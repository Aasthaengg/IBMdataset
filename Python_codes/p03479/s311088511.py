a, b = map(int, input().split())
cnt=0
while a <=b:
  cnt+=1
  a = a*2
print(cnt)