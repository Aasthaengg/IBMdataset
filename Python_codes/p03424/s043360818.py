n=int(input())
l=list(map(str,input().split()))

for i in range (n):
  if l[i]=='Y':
    print('Four')
    exit()
print('Three')


