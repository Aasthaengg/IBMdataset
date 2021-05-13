h,w,n = map(int,input().split())

from collections import defaultdict
dic = defaultdict(int)
for _ in range(n):
   a,b = map(int,input().split())
   a -= 1
   b -= 1
   for aa in range(a-1, a+2):
      for bb in range(b-1, b+2):
         if 1 <= aa <= h-2 and 1 <= bb <= w-2:
            dic[(aa,bb)] += 1
ans = [0 for i in range(10)]
for i in dic.values():
   ans[i] += 1

ans[0] = (h-2)*(w-2) - sum([ans[i] for i in range(1,10)])

for anss in ans:
   print(anss)