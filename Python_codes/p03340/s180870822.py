N=int(input())
A=list(map(int,input().split()))
l=[-1]*20
a=0
t=-1
for i in range(N):
    for j in range(20):
        if (A[i]>>j)%2:
            if t<l[j]:
                t=l[j]
            l[j]=i
    a+=i-t
print(a)