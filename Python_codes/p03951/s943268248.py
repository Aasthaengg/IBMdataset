N = int(input())
s = input()
t = input()

ans = N
for i in range(N):
  if s[i:] == t[:N-i]:
     print(ans)
     exit()
  else:
    ans += 1
  
print(ans)