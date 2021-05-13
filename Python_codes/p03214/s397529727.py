n = int(input())
l = list(map(int, input().split()))
avg = sum(l)/n
idx=0
mindiff=101
for i,j in enumerate(l):
  if abs(avg-j)<mindiff:
    mindiff = abs(avg-j)
    idx = i
print(idx)