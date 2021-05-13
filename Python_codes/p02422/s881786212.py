string=input()
q=int(input())
for i in range(q):
    lst=input().split()
    order=lst[0]
    if order=='reverse':
        a=int(lst[1])
        b=int(lst[2])
        extraction=''
        for l in range(a,b+1):
            letter=string[l]
            extraction+=letter
        oppose=extraction[::-1]
        lst=list(string)
        lst[a:b+1]=oppose
        string="".join(lst)
    if order=='replace':
        a=int(lst[1])
        b=int(lst[2])
        p=lst[3]
        move=p
        lst=list(string)
        lst[a:b+1]=move
        string="".join(lst)
    if order=='print':
        a=int(lst[1])
        b=int(lst[2])
        extraction=''
        for o in range(a,b+1):
            letter=string[o]
            extraction+=letter
        print(extraction)
