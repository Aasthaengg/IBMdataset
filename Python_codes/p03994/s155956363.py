alphabet = list("abcdefghijklmnopqrstuvwxyz")
s = list(input())
S = [alphabet.index(x) for x in s]
K = int(input())
tmp = K
i = 0
while i < len(S) and tmp > 0:
  if S[i] != 0 and 26-S[i] <= tmp:
    tmp -= 26-S[i]
    S[i] = 0
  i += 1
if tmp > 0:
  S[-1] = (S[-1]+tmp)%26
print("".join([alphabet[x] for x in S]))
