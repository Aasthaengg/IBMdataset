N = int(input())
A= list(map(int,input().split()))
Q = int(input())
heavy = [0] * (10 ** 5 + 1)
for i in A:
  heavy[i] += 1
s = sum(A)
for i in range(Q):
  be,af = map(int,input().split())
  s -= be * heavy[be]
  s += af * heavy[be]
  heavy[af] += heavy[be]
  heavy[be] = 0
  print(s)