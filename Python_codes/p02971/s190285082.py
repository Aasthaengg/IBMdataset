n=int(input())
a=[]
for i in range(n):
  a.append(int(input()))

sort_a = sorted(a, reverse=True)
max_a = sort_a[0]
max_a_1 = sort_a[1]

for i in range(n):
  if a[i] == max_a:
    print(max_a_1)
  else:
    print(max_a)
