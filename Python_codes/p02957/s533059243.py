a, b = map(int, input().split())
A = (a+b)/2
print(int(A) if (a+b)%2==0 else "IMPOSSIBLE")