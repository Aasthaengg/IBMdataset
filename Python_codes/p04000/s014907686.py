H, W, N = map(int, input().split())
 
Dic = {}
for i in range(N):
    a, b = map(int, input().split())
    for j in range(3):
        for k in range(3):
            if 1 <= a-j <= H-2 and 1 <= b-k <= W-2:
                if (a-j, b-k) in Dic:
                    Dic[(a-j, b-k)] += 1
                else:
                    Dic[(a-j, b-k)] = 1
                    
Painted = [0 for _ in range(10)]
colered = 0

for i in Dic:
    Painted[Dic[i]] += 1
    colered += 1

#最後に黒が一か所も塗られていない場所を、総和-(1ヵ所以上黒)として求める
Painted[0] = (H-2) * (W-2) - colered
 
for i in Painted:
    print(i)