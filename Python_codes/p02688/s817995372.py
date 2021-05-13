N, K = map(int, input().split())
sunuke_who_has_sweets = set()
for i in range(K):
  d = int(input())
  sunuke_who_has_sweets |= set(map(int, input().split()))
print(N - len(sunuke_who_has_sweets))