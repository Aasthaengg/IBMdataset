S = input()
w = int(input())
num = len(S)
ans = []
for i in range(0, num, w): ans += S[i]
print(''.join(ans))
