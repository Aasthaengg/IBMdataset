n = int(input())
l = list(map(int, input().split()))
c = 0
for i in l:
  c += 1/i
print(1/c)