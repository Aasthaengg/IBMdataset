from collections import Counter
N,K,Q = map(int,input().split())
A_list = []
for _ in range(Q):
  A = int(input())
  A_list.append(A)
A_Counter = Counter(A_list)
for i in range(1,N+1):
  print("Yes" if K + A_Counter[i] - Q > 0 else "No")