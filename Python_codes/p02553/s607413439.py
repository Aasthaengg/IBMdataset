# 21:17-                                                                                                                                                      
a, b, c, d = map(int, input().split())

cands = [a*c, a*d, b*c, b*d]
if a * b <= 0 or c * d <= 0:
    cands.append(0)

print(max(cands))