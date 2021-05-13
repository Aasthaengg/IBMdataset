A, B, C, D, E, F = map(int, input().split())
import math

candicate=[]
for weia in range(0,F+1,100*A):
    for weib in range(0,F+1,100*B):
        water=weia + weib
        if 0 <water <= F:
            salm=water//100*E
            for salc in range(0,salm+1,C):
                for sald in range(0,salm+1,D):
                    salt=salc+sald
                    if salt <= salm and water+salt <= F:
                        #print(weia, weib, salc, sald)
                        candicate.append((water, salt))
#print(candicate)
max_pair=max(candicate, key=lambda x:x[1]/sum(x))
#print(max_pair)
print(sum(max_pair), max_pair[1])