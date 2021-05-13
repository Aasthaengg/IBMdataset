n = int(input())

abl = []
for _ in range(n):
   a,b = map(int,input().split())
   abl.append((a,b))

abl = sorted(abl, reverse=True)

print(sum(abl[0]))