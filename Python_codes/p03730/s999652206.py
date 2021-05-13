a, b, c = map(int, input().split())
l = []
for i in range(1, b+1):
    l.append((a*i)%b)
if c in l:
    print("YES")
else:
    print("NO")