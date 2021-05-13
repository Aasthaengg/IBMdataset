n = int(input())
p = list(map(int,input().split()))
#print(p[:3])
p_cut =[]
cnt = 0

for i in range(n-2):
    p_cut = p[i:i+3]
    #print(p_cut)
    if p_cut[1] != max(p_cut)and p_cut[1] != min(p_cut):
        cnt += 1
print(cnt)