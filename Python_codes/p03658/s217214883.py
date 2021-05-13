N , K  = map(int,input().split())
l = [int(x) for x in input().split()]
l = sorted(l)
猫 = 100
# l = reversed(l)
l.reverse()
for i in range(K):
  猫 += l[i]
print(猫-100)