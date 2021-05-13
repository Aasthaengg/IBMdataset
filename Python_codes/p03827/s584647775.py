N = int(input())
S = input()
a = 0
sum_a = 0

for i in range(N):
  if S[i]=="I":
    sum_a += 1 
    a = max (a , sum_a)
  else:
    sum_a -= 1
print(a)