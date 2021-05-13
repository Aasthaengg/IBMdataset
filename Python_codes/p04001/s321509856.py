def func(i,x,s,new):
    if i==x:
        count=0
        #print(i,x,s,new+[s[-1]])
        new+=s[-1]
        li=new.split("+")
        for j in li:
            count+=int(j)

        return count

    #print(i,x,s,new)
    return func(i,x+1,s,new+s[x-1]+"+") + func(i,x+1,s,new+s[x-1])

new=""
S=input()
print(func(len(S),1,S,new))
