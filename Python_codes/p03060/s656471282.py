N = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))

ben = 0
for i in range(N):
  each_ben = V[i] - C[i]
  if each_ben > 0:
    ben += each_ben
print(ben)