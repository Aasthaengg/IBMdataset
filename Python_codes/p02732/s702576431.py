from collections import Counter

n= int(input())
a=list(map(int,input().split()))
ca = Counter(a)
sa = set(a)
sum_ans=0
for i in sa:
  sum_ans+=(ca[i]*(ca[i]-1))//2

for i in a:
  print(sum_ans-(ca[i]*(ca[i]-1))//2+((ca[i]-1)*(ca[i]-2))//2)