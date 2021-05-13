S=input()
ans=754
for i in range(len(S)-2):
  n=abs(753-int(''.join(list(S[i:i+3]))))
  ans=min(ans,n)
print(ans)