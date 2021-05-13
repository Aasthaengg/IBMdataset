A, B = map(int, input().split())
ans = "IMPOSSIBLE"
if (A+B)%2 == 0:
    ans = int((A+B)/2)
print(ans)