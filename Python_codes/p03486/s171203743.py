s = input()
t = input()

news=''.join(sorted(s))
newt=''.join(sorted(t, reverse=True))
mylist=[news,newt]
mylist=sorted(mylist)

if news==newt:
    print("No")
    exit()

if mylist[0]==news:
    print("Yes")
else:
    print("No")