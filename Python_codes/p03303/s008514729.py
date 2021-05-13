S = input()
N = int(input())
result = []
for i in range(0,len(S),N):
  result.append(S[i])
print("".join(result))