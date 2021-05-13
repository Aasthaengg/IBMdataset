N = int(input())
abcde = [int(input()) for _ in range(5)]
mx = min(abcde)
if N % mx == 0:
  ans = 5 + N // mx -1
else:
  ans = 5 + N // mx

print(ans)