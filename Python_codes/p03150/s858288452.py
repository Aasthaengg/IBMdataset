s=input()
n=len(s)
k="keyence"
for i in range(n):
  for j in range(i,n):
    t=s[:i]+s[j:]
    if k==t:
      print("YES")
      exit(0)
print("NO")
