from collections import defaultdict
dic = defaultdict(int)

for _ in range(3):
    a,b = map(int,input().split())
    dic[a] += 1
    dic[b] += 1

for i in dic.values():
   if i == 3:
       print("NO")
       exit()
print("YES")