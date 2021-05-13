n = int(input())
dict1 = {}
ans = 0

# nを素因数分解したリストを返す
def prime_decomposition(n):
  i = 2
  table = []
  while i * i <= n:
    while n % i == 0:
      n //= i
      table.append(i)
    i += 1
  if n > 1:
    table.append(n)
  return table

for i in range(1,n+1):
    t = prime_decomposition(i)
    for j in t:
        if j in dict1:
            dict1[j] += 1
        else:
            dict1[j] = 1

dict1_sorted = sorted(dict1.items(), key=lambda x:x[0])

li = []
for i in dict1_sorted:
    if i[1] >= 2:
        li.append(i)

m = len(li)

for i in li:
    if i[1] >= 74:
        ans += 1
    else:
        break

for i in li:
    for j in li:
        if i[0] != j[0]:
            if i[1] >= 2 and j[1] >= 24:
                ans += 1
            if i[1] >= 4 and j[1] >= 14:
                ans += 1

ans2 = 0

for i in li:
    for j in li:
        for k in li:
            if i[0] != j[0] and j[0] != k[0] and k[0] != i[0]:
                if i[1] >= 2 and j[1] >= 4 and k[1] >= 4:
                    ans2 += 1

ans += ans2 // 2

print(ans)
