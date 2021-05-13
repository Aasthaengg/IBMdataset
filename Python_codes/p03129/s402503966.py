n,k = map(int,input().split())
frag = 0
if n%2 == 0:
    frag = n//2
else:
    frag = (n//2) + 1

if k > frag:
    print("NO")
else:
    print("YES")