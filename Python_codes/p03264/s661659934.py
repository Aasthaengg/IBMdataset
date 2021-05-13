N = int(input())
n = -(-N // 2)
ans = n * n
if N % 2 != 0:
    ans -= n
print(ans)
