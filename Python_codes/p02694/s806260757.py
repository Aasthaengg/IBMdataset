maxt = int(input())
t,nen = 100,0
while t<maxt:
    t += t//100
    nen += 1
print(nen)    
