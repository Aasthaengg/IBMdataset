n = int(input())
b = list(map(int,input().split()))
rev = []
for i in range(n): #i番目の操作のものを見つける
    cand = []
    for j in range(len(b)):
        if b[j] != j+1:
            if cand:
                continue
            break
        else:
            cand.append(j+1)
    if not cand:
        print(-1)
        exit()
    rev.append(cand[-1])
    b.pop(cand[-1]-1)
ans = reversed(rev)
for k in ans:
    print(k)