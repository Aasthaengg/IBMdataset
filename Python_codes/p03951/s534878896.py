n = int(input())
s = list(input())
t = list(input())

cnt=0
for i in range(n+1)[::-1]:
  if s[-i:]==t[:i]:
    print(n+cnt)
    exit()

  else:
    cnt+=1
print(n*2)
