a = 0

for n in range(int(input())):
  l,r = map(int,input().split())
  a+=r-l+1

print(a)