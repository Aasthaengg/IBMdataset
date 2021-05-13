S = input()
N = len(S)
target = ['A', 'C', 'G', 'T']
ans = []
for i in range(N):
    ret = 0
    for j in S[i:N]:
      if not j in target:
        break
      ret += 1
    ans.append(ret)
    i = j
print(max(ans))