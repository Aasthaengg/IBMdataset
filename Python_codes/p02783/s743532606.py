H, A = map(int, input().split())
for i in range(1, 2*(10**4)):
  H -= A
  if H <= 0:
    break
print(i)