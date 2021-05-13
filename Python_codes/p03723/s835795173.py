ans = 0
A, B, C = map(int, input().split())
while A % 2 == 0 and B % 2 == 0 and C % 2 == 0 and ans < 1000:
        A, B, C = B/2+C/2, C/2+A/2, A/2+B/2
        ans += 1
if ans == 1000:
    print(-1)
else:
    print(ans)

