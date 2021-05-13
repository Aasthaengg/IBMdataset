from sys import exit
x,y=input().split(' ')
groups=[['1','3','5','7','8','10','12'],['4','6','9','11'],['2']]
for group in groups:
  if x in group and y in group:
    print('Yes')
    exit(0)
print('No')