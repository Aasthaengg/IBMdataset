A,B,T = map(int, input().split())
ans = T // A * B
if T % A + 0.5 >= A:
    ans += B
print(ans)