n=int(input())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
maxi=0
for i in range(n):maxi=max(maxi,sum(a1[:i+1]+a2[i:]))
print(maxi)