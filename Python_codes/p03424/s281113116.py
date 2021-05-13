n=int(input())
s=list(input().split())
color=[0]*4
for i in s:
    if i=="P":
        color[0]+=1
    elif i=="W":
        color[1]+=1
    elif i=="G":
        color[2]+=1
    else:
        color[3]+=1
print("Four" if color.count(0)==0 else "Three")