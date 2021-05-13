def isBingo(ary):
  ret = False
  if (
    (ary[0] == ary[1] == ary[2] == 0)
    or (ary[3] == ary[4] == ary[5] == 0)
    or (ary[6] == ary[7] == ary[8] == 0)
    or (ary[0] == ary[3] == ary[6] == 0)
    or (ary[1] == ary[4] == ary[7] == 0)
    or (ary[2] == ary[5] == ary[8] == 0)
    or (ary[0] == ary[4] == ary[8] == 0)
    or (ary[2] == ary[4] == ary[6] == 0)
  ):
    ret = True

  return ret

A = []
for i in range(3):
  row = input().split(" ")
  for n in row:
    A.append(int(n))

B = []
N = int(input())
for i in range(N):
  B.append(int(input()))
  
B = list(set(B))
C = list(map(lambda a: 0 if a in B else a, A))

print("Yes") if isBingo(C) else print("No")