S = input()

count=S.count("W")
a=0
mylist=[]

for i in range(len(S)):
    if S[i]=="W":
        mylist.append(i+1)

for j in range(len(mylist)):
    a=a+mylist[j]-j-1
print(a)