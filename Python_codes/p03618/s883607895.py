s = input()
cnt = [0]*26
n = len(s)
for i in range(n):
  cnt[ord(s[i])-97] += 1
ans = n*(n-1)//2
for i in range(26):
  ans -= (cnt[i]*(cnt[i]-1)//2)
print(ans+1)