N = int(input())
s = [int(input()) for _ in range(N)]
if sum(s) % 10 != 0: print(sum(s)); exit()
else:
  s.sort()
  for i in range(N):
    if (sum(s)-s[i])%10 != 0: print(sum(s)-s[i]); exit()
print(0)