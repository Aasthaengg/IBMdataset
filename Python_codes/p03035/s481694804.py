A, B = list(map(int, input().split()))

if A >= 13:
    ans = B
elif A >= 6:
    ans = B // 2
else:
    ans = 0
print(ans)