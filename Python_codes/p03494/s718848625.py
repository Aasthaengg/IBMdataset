n = int(input())
a = list(map(int, input().split()))
c = 0
while True:
  a = [i//2 for i in a if i%2 == 0]
  if len(a) < n:
    break
  c += 1
print(c)