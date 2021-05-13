I=list(map(int, input().split()))
n=0
for i in I:
  if i==sum(I)/2:
    n+=1
print('No' if n==0 else 'Yes')