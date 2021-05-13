N=int(input())
S=list(input().split())
for s in S:
  if s=='Y':
    print('Four')
    exit(0)
print('Three')