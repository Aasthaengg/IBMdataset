a, b, c = list(map(int, input().split()))
a, b, c = sorted([a, b, c])
ans = 0
ans += c-b
ans += (b-a + 1)//2
if (b-a)%2:
    ans += 1
print(ans)
