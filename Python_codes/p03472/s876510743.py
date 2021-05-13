from operator import itemgetter
import math
N, H = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)] 

ab.sort(key=itemgetter(1), reverse=True)

amax = max([i[0] for i in ab]) 
num = 0
dmg = 0
jdg = False

for a, b in ab:
    if b > amax:
        num += 1
        dmg += b
        if dmg >= H:
            jdg = True
            break
if not jdg:
    num += math.ceil((H - dmg) / amax)
print(num)