S = input()
K = "keyence"
for i in range(len(K)):
  if (K[:i] == S[:i]) and (K[(i-(len(K))):] == S[(i-(len(K))):]):
    print("YES")
    exit()
if K == S[:len(K)] or K == S[(-len(K)):]:
  print("YES")
  exit()
print("NO")
