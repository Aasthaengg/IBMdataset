l=[0]*4
for i in range(3):
    N,M=map(int,input().split())
    l[N-1]+=1
    l[M-1]+=1
print("YES" if max(l)<3 else "NO")