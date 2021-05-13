S=input()
n=len(S)

res = 0
for i in range(n):
  for j in range(i,n):
    sub = S[i:j+1]
    flg=True
    for c in sub:
      if c not in ["A","G","C","T"]:
        flg = False
    if flg:
      res = max(res,len(sub))
print(res)
