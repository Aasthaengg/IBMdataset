N,k = (int(x) for x in input().split())
S = list(input())
if S[k-1] == "A":
  S[k-1] = "a"
elif S[k-1] == "B":
  S[k-1] = "b"
else:
  S[k-1] = "c"
print("".join(S))