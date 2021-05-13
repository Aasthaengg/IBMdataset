a, b, c, d = map(int, input().split())
if a<0:
    candi = a*c
else:
    candi = a*d

if b<0:
    candi2 = b*c
else:
    candi2 = b*d

print(max(candi, candi2))