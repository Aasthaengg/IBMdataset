N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = False

big_a = sum([ai - bi for ai, bi in zip(a,b) if ai > bi])
big_b = sum([(bi - ai) // 2 for ai, bi in zip(a,b) if bi > ai])
sum_diff = sum(b) - sum(a)

if big_a <= big_b:
  result = True

ans = "Yes" if result else "No"
print(ans)