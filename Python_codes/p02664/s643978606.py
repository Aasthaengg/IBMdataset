s = str(input())
s_ = list(s)
for i in range(len(s)):
  if s_[i]=='?':
    s_[i]='D'
S = "".join(s_)
print(S)