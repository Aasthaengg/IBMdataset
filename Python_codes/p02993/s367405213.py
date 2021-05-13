S=input()
i=[]
i.extend(S)
if i[0]==i[1]:
        print('Bad')
elif i[1]==i[2]:
        print('Bad')
elif i[2]==i[3]:
        print('Bad')
else:
    print('Good')