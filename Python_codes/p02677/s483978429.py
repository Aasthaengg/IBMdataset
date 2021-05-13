import math

lh, lm, h, m = (int(i) for i in input().split())
ang1 = 360 / 12 * h + (30 / 60) * m
ang2 = 360 / 60 * m
ang = abs(ang1 - ang2)
#print(ang)
ang = ang / 360 * 2 * math.pi
#print(ang)
sq = lh**2 + lm**2 - 2 * lh * lm * math.cos(ang)
print(math.sqrt(sq))
