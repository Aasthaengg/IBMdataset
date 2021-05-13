K,S = (int(x) for x in input().split())
count = 0
for x in range(K+1):
  for y in range(K+1):
    remain = S-x-y
    if 0 <= remain and remain <= K:
      count += 1

print(count)