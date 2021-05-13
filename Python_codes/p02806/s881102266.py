N=int(input())
name=["" for _ in range(N+1)]
time=[0 for _ in range(N+1)]
for i in range(N):
    n,t=input().split()
    name[i+1]=n
    time[i+1]=time[i]+int(t)
print(time[N]-time[name.index(input())])