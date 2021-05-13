a,b = [int(x) for x in input().split()]

dif = b - a
org = sum([x for x in range(1,dif)])
print(org-a)