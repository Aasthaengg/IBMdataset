# ume 20/06/21
def dfs(s, seq, res):
  if len(s)==0: return
  for i in range(1, len(s)):
    seq.append(int(s[:i]))
    res[0] += sum(seq) + int(s[i:])
    dfs(s[i:], seq, res)
    seq.pop()
    

S = input()
seq = []
res = [int(S)]
dfs(S, seq, res)
print(res[0])