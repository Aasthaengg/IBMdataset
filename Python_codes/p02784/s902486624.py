H, N = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse = True)

for i in A:
  H -= i
  if H <= 0:
    print('Yes')
    exit()

print('No')