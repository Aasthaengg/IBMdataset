import math

S = input()
w = int(input())

t = math.ceil(len(S) / w)
ans = ""
for i in range(t):
    ans = ans + S[i*w]
print(ans)