def split(a): 
    return [char for char in a]    
pred=input()
real=input()
x=split(pred)
y=split(real)
c=0
if x[0]==y[0]:
    c+=1
if x[1]==y[1]:
    c+=1
if x[2]==y[2]:
    c+=1
print(c)