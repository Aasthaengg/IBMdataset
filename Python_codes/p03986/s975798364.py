X=input()
stack=[]
point=0
for i in range(len(X)):
    if X[i]=="S":
        stack.append(X[i])
        point+=1
    else:
        if point==0:
            stack.append(X[i])
            point+=1
        elif stack[point-1]=="T":
            stack.append(X[i])
            point+=1
        elif stack[point-1]=="S":
            del stack[point-1]
            point-=1
print(len(stack))