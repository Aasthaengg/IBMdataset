N=int(input())
S=input()
cnt=[1]*26
for i in range(len(S)):
  cnt[ord(S[i])-ord('a')]+=1
ans=1
for i in range(26):
  ans*=cnt[i]
print((ans-1)%(10**9+7))
