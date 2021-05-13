n=int(input())
c=0
for i in input().split():
  c+=int(i)
print("YES" if c%2==0 else "NO")