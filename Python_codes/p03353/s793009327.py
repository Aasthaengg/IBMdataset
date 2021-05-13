import sys
input = sys.stdin.readline
s = input().rstrip()
l = len(s)
k = int(input())
chk = set()
for i in range(26):
  for j in range(l):
    if s[j] == chr(i+97):
      for m in range(min(5,l-j)):
        chk.add(s[j:j+1+m])
  if len(chk) >= k:
    break
    
chk = sorted(list(chk))
print(chk[k-1])