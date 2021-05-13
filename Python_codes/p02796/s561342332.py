N = int(input())
A=[]
for _ in range(N):
    x,l = map(int,input().split())
    A.append([x-l,x+l])
A = sorted(A, key=lambda x:x[1])
now = -10**10
cnt = 0
for x in A:
    if now <= x[0]:
        now = x[1]
        cnt+=1
print(cnt)

