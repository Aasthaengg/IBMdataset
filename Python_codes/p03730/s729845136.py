a,b,c = map(int,input().split())
x = a%b
found = False
for i in range(b):
  if (x*i)%b == c:
    found = True
    break
print("YES" if found else "NO")