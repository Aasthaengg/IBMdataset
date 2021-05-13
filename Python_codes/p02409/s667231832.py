R=range
l=[[[0 for i in R(10)]for j in R(3)]for s in R(4)]
n=int(input())
for a in range(n):
    b,f,r,v=map(int,input().split())
    l[b-1][f-1][r-1]+=v
for b in range(4):
    for k in l[b]:
        print('',*k)
    if b<3:
        print('#'*20)