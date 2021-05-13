N = int(input())
A, B = map(int,input().split())
P = list(map(int,input().split()))
prob1 = 0
prob2  =0
prob3 = 0
for i in P: 
  if i <= A: prob1 += 1
  elif B + 1 <= i: prob3 += 1
  else: prob2 += 1
print(min(prob1,prob2,prob3))    