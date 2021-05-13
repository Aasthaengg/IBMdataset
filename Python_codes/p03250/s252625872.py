l = [int(i) for i in input().split()]
l.sort(reverse=True)
print(l[0]*10 + l[1] + l[2])