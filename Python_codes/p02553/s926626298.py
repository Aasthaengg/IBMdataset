a,b,c,d = [int(i) for i in input().split()]

M = max(a*c, a*d, b*c, b*d)
print(str(M))