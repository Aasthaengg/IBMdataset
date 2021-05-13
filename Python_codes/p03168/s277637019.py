N = int(input())
P = list(map(float, input().split()))
import numpy as np
def prob_ret():
  prob = [0.0]*(N+1)
  prob[0] = 1
  prob=np.array(prob)
  for n in range(N):
    p = prob[:N]*P[n]
    prob = prob * (1-P[n])
    prob[1:] = prob[1:] + p
  return sum(prob[N//2+1:])
print(prob_ret())