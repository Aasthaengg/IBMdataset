from collections import Counter
h,w=map(int,input().split())
cnt=Counter()
for i in range(h):
  c=Counter(input())
  cnt+=c
sum1=0
sum2=0
sum4=0
for i in cnt.values():
  sum1+=i%2
  sum4+=i//4
  sum2+=(i-(i//4)*4)//2
if h%2==0 and w%2==0:
  print('Yes' if sum1==0 and sum2==0 else 'No')
elif h%2==1 and w%2==1:
  print('Yes' if sum1==1 and sum4>=((w-1)*(h-1))/4 else 'No')
elif h%2==1 and w%2==0:
  print('Yes' if sum1==0 and sum2<=w/2 else 'No')
else:
  print('Yes' if sum1==0 and sum2<=h/2 else 'No')