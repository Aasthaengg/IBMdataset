N, X, Y = map(int, input().split())
ans =  X+Y-N
if ans < 0:
    ans = 0
print(min(X,Y), ans)