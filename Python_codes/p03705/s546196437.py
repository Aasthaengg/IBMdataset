n,a,b = map(int, input().split())
if (n == 1 and a != b) or (a>b):
    Ans = 0
else:
    Ans = (b - a) * (n - 2) + 1
print(Ans)