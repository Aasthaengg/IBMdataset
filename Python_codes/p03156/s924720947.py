n=int(input())
a,b=[int(s) for s in input().split()]
P=[int(s) for s in input().split()]

lea=[p for p in P if p<=a]
gealeb=[p for p in P if a<p<=b]
gtb=[p for p in P if p>b]

print(min(len(lea),len(gealeb),len(gtb)))