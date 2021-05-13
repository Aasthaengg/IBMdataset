l = list(map(int, input().split()))
l.sort()
t = l[-1]
l[-1]-=1
t += max(l[0],l[1])
print(t)