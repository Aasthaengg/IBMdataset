S = str(input())
N = len(S)
A = set(["A","C","T","G"])
Flag = True
ans = 0
ret = 0
for i in range(N):
  if S[i] in A:
    if Flag:
      ans += 1
    else:
      ans = 0
  else:
    ans = 0
  ret = max(ret,ans)
print(ret)    