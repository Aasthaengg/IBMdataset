string=input()
list=[]
for i in range(0,len(string)):
         if string[i] not in list:
            list.append(string[i])

         if string[i] not in list:
            list.append(string[i])

if(len(list)==2):
    print("Yes")
else:
    print("No")
