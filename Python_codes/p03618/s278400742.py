import string

S = input()
ans = len(S)*(len(S)-1)//2 + 1
for i in string.ascii_lowercase:
  c = S.count(i)
  ans -= c*(c-1)//2
print(ans)
