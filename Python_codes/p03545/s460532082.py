s=input()
n=4-1
for i in range(1<<n):
    lst=list(s)
    for j in range(n):
        if ((i>>j)&1):
            lst.insert(2*j+1,"+")
            # print(lst)
        else:
            lst.insert(2*j+1,"-")
    if(eval("".join(lst))==7):
        print(("".join(lst))+"=7")
        break