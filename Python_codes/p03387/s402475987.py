A,B,C = map(int,input().split())

cnt = 0
A,B,C = sorted([A,B,C])
i = C - B
cnt += i
B += i
A += i

j = C - A
if j % 2 == 0:
  cnt += j // 2
else:
  cnt += j // 2 + 2
  
print(cnt)