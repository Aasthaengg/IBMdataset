N=int(input())
A=list(map(int,input().split()))
f=0
for a in A:
    f=f^a
print("Yes" if f==0 else "No")