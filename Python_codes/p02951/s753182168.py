a,b,c = map(int,input().split())
e = a - b
ans = c - e
print(ans if ans > 0 else "0")
