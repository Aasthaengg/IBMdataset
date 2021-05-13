a,b,c = map(int, input().split())
d = c-a-b
if d <= 0: print("No")
else: print("Yes" if 4*a*b < d**2 else "No")