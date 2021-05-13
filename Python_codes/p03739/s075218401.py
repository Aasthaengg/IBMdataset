N = int(input())
A = list(map(int, input().split()))
B = [A[0]]
for i in range(1,N):
  A[i] += A[i-1]

th = min(0, A[0]-1)
ans_pos = abs(th) #正スタート
for i in range(1,N):
  if i % 2 == 1: #負にしたい
    ans_pos += abs(th - max(th, A[i]+1))
    th = max(th, A[i]+1)
  else: #正にしたい
    ans_pos += abs(th - min(th, A[i]-1))
    th = min(th, A[i]-1)
  #print(ans_pos, th, i)

th = max(0, A[0]+1)
ans_neg = abs(th) #負スタート
for i in range(1,N):
  if i % 2 == 1: #正にしたい
    ans_neg += abs(th - min(th, A[i]-1))
    th = min(th, A[i]-1)
  else: #負にしたい
    ans_neg += abs(th - max(th, A[i]+1))
    th = max(th, A[i]+1)
  #print(ans_neg, th, i)

print(min(ans_pos, ans_neg))