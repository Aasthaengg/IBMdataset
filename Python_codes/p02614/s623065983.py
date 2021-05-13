from itertools import combinations

h,w,k = map(int,input().split())
c = [list(input()) for _ in range(h)]

ans = 0
for i in range(h+1):
  for j in range(w+1):
    for ci in combinations(list(range(h)),i):
      for cj in combinations(list(range(w)),j):
        cnt = 0
        for l in ci:
          for m in cj:
            if c[l][m] == "#":
              cnt += 1
        if cnt == k:
          ans += 1
print(ans)