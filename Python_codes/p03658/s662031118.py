a,b = map(int,input().split())
l = sorted(list(map(int,input().split() )))[::-1]
sum = 0
for i in range(b):
  sum += l[i]
print(sum)