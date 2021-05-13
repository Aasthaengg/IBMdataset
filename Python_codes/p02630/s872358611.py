N = int(input())
A = list(map(int, input().split()))
Q = int(input())
List = [0 for _ in range(10**5)]
for x in A:
  List[x-1] += 1
ans = sum(A)
for i in range(Q):
  B, C = map(int, input().split())
  if List[B-1] != 0:
    ans += (C-B)*List[B-1]
    List[C-1] += List[B-1]
    List[B-1] = 0
  print(ans)