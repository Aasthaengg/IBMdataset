import itertools
n=int(input())
a=list(map(int,input().split()))
gusu=0
for i in a:
  if i%2==0:
    gusu+=1
print(3**n-2**gusu)