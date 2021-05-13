N = int(input())
A,B = map(int,input().split())
P = list(map(int,input().split()))
#P.sort()
q1 = []
q2 = []
q3 = []
for i in range(N):
  if P[i] <= A:
    q1.append(P[i])
  elif P[i] <= B:
    q2.append(P[i])
  else:
    q3.append(P[i])
print(min(len(q1),len(q2),len(q3)))