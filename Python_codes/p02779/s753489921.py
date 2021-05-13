N=int(input())

A=list(map(int,input().split()))

S=set()
for i in A:
    S.add(i)

if len(S)==len(A):
    print("YES")
else:
    print("NO")