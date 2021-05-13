n,m = map(int,input().split())
L = [0]*m; R = [0]*m; cnt = 0
for i in range(m):
    L[i],R[i] = map(int,input().split())
ml = max(L); mr = min(R)
print(mr-ml+1) if ml <= mr else print(0)