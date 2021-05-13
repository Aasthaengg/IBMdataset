list=input()
newlist=[list[i:i+1] for i in range(0,len(list))]
for n in range(0,len(newlist)):
 if newlist[n]=="?":
  newlist[n]="D"
print(''.join(newlist))
