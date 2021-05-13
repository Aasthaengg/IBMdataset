a, b, k = map(int, input().split())
ans = []
for i in range(k):
  if a + i <= b:
    ans.append(a + i)
  if b - i >= a:
    ans.append(b - i) 
for i in sorted(set(ans)):
    print(i)