n = int(input())
a = list(map(int,input().split()))

m = max(a)
#約分できちゃう数値リスト
lis = [0]*(m + 1)
for i in a:
  for j in range(i, m + 1, i):
    lis[j] += 1
#iが1なら、lisの要素全てに+1されてる。
count = 0
for i in a:
  if lis[i] == 1:
    count += 1
    
print(count)