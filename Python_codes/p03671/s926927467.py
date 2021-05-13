l = list(map(int, input().split()))
print(min(sum(l[:2]), sum(l[1:]), l[0]+l[2]))