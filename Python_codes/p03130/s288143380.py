cnt = [0 for _ in range(4)]
for _ in range(3):
  a,b = map(int,input().split())
  cnt[a-1] += 1
  cnt[b-1] += 1

print('YES' if 1<=min(cnt) and max(cnt)<=2 else 'NO')