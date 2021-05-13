a, b, c = map(int, input().split())

noeat = c-(a+b+1) if c > (a+b) else 0
print(c+b-noeat)
