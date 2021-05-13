N = int(input())
A = list(map(int, input().split()))

sum_A = 0
for item in A:
  sum_A ^= item

ans = [str(sum_A ^ item) for item in A]
print(" ".join(ans))