a,b,c,d = map(int,input().split())
l1 = abs(a-b)
l2 = abs(a-c)
l3 = abs(b-c)
print("Yes" if l2 <= d or (l1 <= d and l3 <= d) else "No")