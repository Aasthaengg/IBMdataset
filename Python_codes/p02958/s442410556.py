N = int(input())
p = list(map(lambda x: int(x), input().split(" ")))

cnt = 0
for i in range(len(p)):
  cnt += 1 if p[i] != i + 1 else 0

print("YES") if cnt in [0, 2] else print("NO")