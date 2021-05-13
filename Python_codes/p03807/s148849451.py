N=int(input())
A=list(map(int,input().split()))
s=0
for i in A:
    if i%2:
        s+=1
print("YES" if s%2==0 else "NO")