S = input()
Q = int(input())
flip = 0
head = []
tail = []
for i in range(Q):
  Query = input().split()
  if len(Query) == 3:
    T,F,C = Query
    F = int(F)-1
    if F^flip == 1:
      tail.append(C)
    else:
      head.append(C)
  else:
    flip ^= 1
if flip:
  head, tail = tail, head
  S = S[::-1]
head = ''.join(head[::-1])
tail = ''.join(tail)
print(head+S+tail)