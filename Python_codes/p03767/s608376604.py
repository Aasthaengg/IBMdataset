N=int(input())
a=list(map(int,input().split()))

a.sort()
a.reverse()

A=a[1:(2*N):2]

print(sum(A))