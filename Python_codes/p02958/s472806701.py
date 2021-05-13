N = int(input())
P = list(map(int,input().split()))

new_list = sorted(P)
cnt=0
for i,e in zip(P,new_list):
  if i != e:
    cnt+=1

if cnt == 2 or cnt == 0:
  print('YES')
else:
  print('NO')
