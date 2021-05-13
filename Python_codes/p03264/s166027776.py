x=range(1,int(input())+1)
y=[t for t in x if t%2==0]
z=[t for t in x if t%2==1]
print(len(y)*len(z))