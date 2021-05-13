n = input()
l = [int(x) for x in input().split()]
cnt = 0
while len([True for x in l if x%2==0]) == len(l):
  l = [x/2 for x in l]
  cnt += 1
print(cnt)