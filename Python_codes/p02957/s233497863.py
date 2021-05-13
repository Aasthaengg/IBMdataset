a,b = map(int, input().split())
x = a +b
print(int(x/2) if x%2 == 0 else "IMPOSSIBLE")