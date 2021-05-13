n=int(input())
s=list(map(int,input().split()))
z=0
for i in range(n):
  for j in range(i+1,n):
    z+=s[i]*s[j]
print(z)