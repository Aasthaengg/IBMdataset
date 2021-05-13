n=int(input())
t=list(map(int,input().split()))
sum_t=sum(t)
d=int(input())
for _ in range(d):
    p,time=map(int,input().split())
    print(sum_t-t[p-1]+time)