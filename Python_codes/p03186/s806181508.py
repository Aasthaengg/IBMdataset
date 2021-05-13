A,B,C = map(int,input().split())


if A+B < C:
    ans = (A+B) + B + 1
else:
    ans = B+C

print(ans)
