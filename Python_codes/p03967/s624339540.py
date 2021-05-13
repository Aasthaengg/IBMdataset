s = str(input())
n = len(s)
hand = 0
point = 0
for i in range(n):
    if i==0:
        hand +=1
        continue
    if s[i]=="p" and hand>0:
        hand -=1
    elif s[i]=="p" and hand ==0:
        hand +=1
        point-=1
    elif s[i]=="g" and hand>0:
        hand -=1
        point +=1
    elif s[i]=="g" and hand==0:
        hand +=1
print(point)
