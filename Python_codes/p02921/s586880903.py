S=input()
T=input()
result=0
i=[]
n=[]
i.extend(S)
n.extend(T)
if i[0]==n[0]:
    result+=1
if i[1]==n[1]:
    result+=1
if i[2]==n[2]:
    result+=1
print(result)