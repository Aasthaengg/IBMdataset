
str=raw_input().strip().split()
list=list()


ans=0
for ss in str:
    if ss=="*":
        a=list.pop()
        b=list.pop()
        list.append(a*b)
    elif ss=="+":
        a=list.pop()
        b=list.pop()
        list.append(a+b)

    elif ss=="-":
        a=list.pop()
        b=list.pop()
        list.append(b-a)
        
    else:
        list.append(int(ss))
   
    
print list.pop()
