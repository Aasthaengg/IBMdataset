import math
S = input()
w = int(input())

count = math.ceil(len(S) / w)

ans = ''
for i in range(count):
    ans += S[i*w]

print(ans)
