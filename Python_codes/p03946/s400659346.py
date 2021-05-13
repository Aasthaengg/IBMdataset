n, t = map(int, input().split())
*a, = map(int, input().split())
purchase = a[0]
profit = []
for i in range(len(a)):
  profit.append(a[i] - purchase)
  if a[i] < purchase:
    purchase = a[i]
profit.sort()
Answer = profit.count(profit[-1])
print(Answer)