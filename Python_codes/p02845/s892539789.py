N = int(input())
A = list(map(int, input().split()))

kMod = 10**9+7

mem = [0, 0, 0]
cnt = 1

for a in A:
   if a not in mem:
       cnt = 0
       break
   cnt *= mem.count(a)
   cnt %= kMod
   mem[mem.index(a)] = a+1
print(cnt)