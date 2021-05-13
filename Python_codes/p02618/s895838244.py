D = int(input())
C = list(map(int, input().split()))
S = []
N = 26
for d in range(D):
    S += [list(map(int, input().split()))]
#print(C)
#print(S)
myans = [d%N for d in range(D)]
for d in range(D):
  print(myans[d]+1)