S,T,operation = input(), input(),0
for i in range(len(S)):
   if S[i]!=T[i]: operation+=1    
print(operation)