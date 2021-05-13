a,b,c = (int(x) for x in input().split())
d = c-(a-b)
print(d if d >= 0 else 0)