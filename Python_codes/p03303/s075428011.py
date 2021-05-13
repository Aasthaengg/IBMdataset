import math
S = input()
w = int(input())
k = []
ans = ""
ans_2 = ""
for i in range(math.ceil(len(S)/w)):
  ans += S[i*w]
print(ans)