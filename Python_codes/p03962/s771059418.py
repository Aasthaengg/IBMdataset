a = list(map(int, input().split()))

l = [0]*101

for i in a:
  l[i] += 1

print(len(list(filter(lambda x: x !=0, l))))