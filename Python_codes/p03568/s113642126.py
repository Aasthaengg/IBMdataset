N =int(input())
AAA = map(int,input().split())
AA = list(AAA)
total = 3**len(AA)
total2 = 0
total3 = 0
for i in AA:
  if i%2==0:
    total2 +=1
total3 = 2**total2
ans = total - total3
print(ans)