AB=[list(map(int,input().split())) for _ in range(3)]

tmp=[]
for a,b in AB:
  tmp.append(a)
  tmp.append(b)
for i in set(tmp):
  if tmp.count(i)==3:
    print('NO')
    exit()
print('YES')