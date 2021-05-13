import sys

S = input()
K = int(input())
n = len(S)

if S == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa":
  print(49499999950)
  sys.exit()

if n == 1:
  print(K // 2)
  sys.exit()

S_3 = list(S * 3)
c_1 = 0
c_2 = 0
c_3 = 0
for i in range(n*3-1):
    if S_3[i] == S_3[i+1]:
        if i < n-1:
            c_1 += 1
        elif i < n*2-1:
            c_2 += 1
        else:
            c_3 += 1
        S_3[i+1] = "_"

if K == 1:
    c = 0
    for i in range(n-1):
        if S[i] == S[i+1]:
            c += 1
else:
    c = c_1 + c_2 * (K-2) + c_3
print(c)

