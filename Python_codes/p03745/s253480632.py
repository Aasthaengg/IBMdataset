import sys
input = sys.stdin.readline

# A - Sorted Arrays
import copy

N = int(input())
A = list(map(int, input().split()))

arr = []
ans = []
# 0: どっちの可能性もある
# 1: 単調非減少(増加)
# 2: 単調非増加(減少)
status = 0

for i in range(N):
  if status == 0:
    if len(arr) > 0:
      if A[i] > arr[-1]:
        status = 1
      elif A[i] < arr[-1]:
        status = 2

    arr.append(A[i])
  elif status == 1 and A[i] >= arr[-1]:
    arr.append(A[i])
  elif status == 2 and A[i] <= arr[-1]:
    arr.append(A[i])
  else:
    ans.append(copy.copy(arr))
    arr = [A[i]]
    status = 0

if len(arr) > 0:
  ans.append(arr)

print(len(ans))

'''
for a in ans:
  print(a)
'''