from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
dic = defaultdict(int)

for t in A:
  dic[t] += 1
#print(dic)
ans = 0
for n,i in dic.items(): #key value
  if n > i:
    ans += i
  elif n < i:
    ans += (i-n)
print(ans)