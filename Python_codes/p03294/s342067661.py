N = int(input())

As = map(int, input().split())

rlt = 0
for a in As:
  rlt += a - 1
  
print(rlt)