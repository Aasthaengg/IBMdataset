a,b,c,d = map(int, input().split())
c1 = abs(a-b) <= d
c2 = abs(b-c) <= d
c3 = abs(c-a) <= d
print("Yes" if c3 or (c1 and c2) else "No")