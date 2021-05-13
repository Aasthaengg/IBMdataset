N = int(input())
B = tuple(map(int, input().split()))
assert len(B) == N - 1

count = B[0] + B[-1]
for b1,b2 in zip(B, B[1:]):
  count += min(b1, b2)
print(count)