n = int(input())
a = [int(input()) for i in range(n)]
sa = sorted(a)
am, asl = sa[-1], sa[-2]
print(*[asl if ai == am else am for ai in a], sep='\n')