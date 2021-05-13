N=int(input())
A=sorted(list(map(int,input().split())))[::-1]
a=0
for i in range(0,N):
    a+=A[1+2*i]
print(a)