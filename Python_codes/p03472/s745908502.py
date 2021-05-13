n,h = map(int,input().split())
slash = []
throw = []
for i in range(n):
    s,t = map(int,input().split())
    slash.append(s)
    throw.append(t)
    
Amax = sorted(slash)[-1]
throw = sorted(throw)
use = [Amax]
for i in range(n):
    if throw[i] > Amax:
        use = [Amax] + throw[i:]
        break

damage = 0
count = 0
while h > damage:
    if use != []:
        damage += use.pop(-1)
        count += 1
    else:
        count += (h-damage)//Amax + ((h-damage)%Amax != 0)
        break
    
print(count)