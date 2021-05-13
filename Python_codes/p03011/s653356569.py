P,Q,R=[int(s) for s in input().split(" ")]

List=[P,Q,R,P]
Ans=[]
SUM=0

for i in range(3):
    SUM=List[i]+List[i+1]
    Ans.append(SUM)
    
print(min(Ans))