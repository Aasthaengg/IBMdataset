n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
d = sorted([v[i]-c[i] for i in range(len(v))])
sum = 0
for i in d[::-1]:
  if sum+i >= sum:
    sum += i
print(sum)
