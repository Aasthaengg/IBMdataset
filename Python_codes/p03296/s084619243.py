N = int(input())
a = list(map(int, input().split()))
changed = [False]*N
count = 0
for num in range(N-1):
  if not changed[num] and a[num] == a[num + 1]:
    changed[num+1] = True
    count += 1
print(count)