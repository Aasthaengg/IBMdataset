N=int(input())
S=input()
nagasa=len(S)
D=[]
goukei=0
for i in range(nagasa-1):
    if S[i+1]=="E":
        goukei+=1
    else:
        goukei+=0
#print(goukei)
     
D.append(goukei)
for i in range(nagasa-1):
    if S[i]=="W":
        goukei+=1
    else:
        goukei+=0
    if S[i+1]== "W":
        goukei+=0
    else:
        goukei-=1
    
    D.append(goukei)
#print(D)
print(min(D))    