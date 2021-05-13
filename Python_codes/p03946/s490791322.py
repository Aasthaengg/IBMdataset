n,t = map(int,input().split())
al = list(map(int,input().split()))

bl = []

min_a = float("inf")
for a in al:
   min_a = min(a, min_a)
   bl.append(min_a)

cl = []

for a,b in zip(al, bl):
   cl.append(a-b)

cl = sorted(cl)

print(cl.count(cl[-1]))