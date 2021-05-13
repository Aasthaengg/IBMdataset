N = int(input())
A = list(map(int,input().split()))

A_=[]
a_=0
for a in A:
    a_+=a
    A_.append(a_)

Z=A_[-1]
ans=10**20
for a_ in A_[:-1]:
    if ans > abs(Z-2*a_):
        ans = abs(Z-2*a_)
print(ans)