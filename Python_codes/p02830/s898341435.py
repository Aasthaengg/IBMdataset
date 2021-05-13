N = int(input())
S,T = input().split()

l = []
for i in range(N):
  l.append(S[i])
  l.append(T[i])
  
print("".join(l))