s=input()
n=int(input())
k=len(s)
ans=""
for i in range(k):
  if i % n==0:
    ans+=s[i]
print(ans)