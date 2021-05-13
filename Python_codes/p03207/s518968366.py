N=int(input())
l=[int(input()) for i in range(N)]
A=max(l)
print(A//2+sum(l)-A)