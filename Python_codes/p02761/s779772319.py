N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
 
# 10^(N-1)から10^Nの数を順に調べる
# N=1の場合のみ、0から10であることに注意
if N == 1:
  a, b = 0, 10
elif N >= 2:
  a, b = 10**(N-1), 10**N

ans = -1
for i in range(a, b):
  tmp = str(i)
  flag = True
  for j in range(M):
    if tmp[arr[j][0]-1] != str(arr[j][1]):
      flag = False
  if flag:
    ans = i
    break

print(ans)
 
# Memo: 0からNの中でM個の条件全てを満たす整数を求めるときは、以下のようにする
'''
a = -1
for i in range(N):
  flag = True
  for j in range(M):
  　　if 条件を満たさない: flag = False
  if flag:
    a = i
    break
print(i)
'''