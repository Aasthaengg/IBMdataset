#N = int(input())
#S = str(input())
#A, B = map(int, input().split())
#C = list(map(int, input().split()))

N, K = map(int, input().split())
S = str(input())

d = ["A", "B", "C"]
e = ["a", "b", "c"]

for i in range(N):
  if i == K - 1:
    inde = d.index(S[i])    
    print(e[inde], end = "")
  else:
    print(S[i], end = "")
