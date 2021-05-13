#入力
lst = input().split()

A = lst[0]
B = lst[1]
C = lst[2]

#出力
if A[-1] == B[0] and B[-1] == C[0]:
   print('YES')
else:
   print('NO')