n = int(input())
h = list(map(int,input().split()))

i = min(h)
ans = i
h = list(map(lambda x:x-i,h))

ck = 0
while sum(h) > 0:
  for i in range(n):
   if h[i] == 0:
     ans += ck
     ck = 0
   else:
     h[i] -= 1
     ck = 1
  else:
   ans += ck
   ck = 0

print(ans)