from bisect import bisect_left as bs
#ソート順序を保ったまま値を挿入する
N, M = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

while M > 0:
  i = A.pop(-1) // 2
  A.insert(bs(A, i), i)
  M -= 1

print(sum(A))