S = input()
K = int(input())

ans = ""
for i in range(min([K, 100, len(S)])):
  if S[i] != "1":
    ans = S[i]
    break

print(ans) if ans else print(1)