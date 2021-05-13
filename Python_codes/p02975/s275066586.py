input()
a=[int(i) for i in input().split()]
ans=0
for i in a:
  ans^=i
print('Yes' if ans==0 else 'No')