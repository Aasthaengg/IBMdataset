N = int(input())
a = []
for i in range(N):
  a.append(int(input()))
a.sort()
count = 1
j = 0
while j < N-1:
  if a[j] != a[j+1]:
    count += 1
  j += 1
print(count)

