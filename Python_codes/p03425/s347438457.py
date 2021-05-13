N = int(input())
S = [0]*5
D = {"M": 0, "A": 1, "R": 2, "C": 3, "H": 4}
for i in range(N):
  name = input()
  if name[0] in "MARCH":
    S[D[name[0]]] += 1
ans = 0
for i in range(0, 3):
  for j in range(i+1, 4):
    for k in range(j+1, 5):
      ans += S[i]*S[j]*S[k]
print(ans)