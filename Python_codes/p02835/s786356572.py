a1=input()
a2=[i for i in a1.split()]
A1,A2,A3=[int(a2[i]) for i in (0,1,2)]
print('bust' if (A1+A2+A3)>=22 else 'win')