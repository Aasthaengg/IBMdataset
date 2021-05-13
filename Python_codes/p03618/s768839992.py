S = input()
N = len(S)

alpha = [0] * 27
for s in S:
  alpha[ord(s) - ord("a")] += 1
#print("alpha:", alpha)

answer = N * (N - 1) // 2 + 1
for a in alpha:
  answer -= (a - 1) * a // 2
print(answer)