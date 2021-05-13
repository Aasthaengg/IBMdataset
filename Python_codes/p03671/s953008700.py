#ringring
a, b, c = map(int, input().split())
S = a + b + c
S = S - max(a,b,c)
print(S)