h,w = map(int, input().split())
rows=[]
for _ in range(h):
  rows.append(list(input().split()))

for i in range(2*h):
  for r in rows[i//2]:
    print(r)
