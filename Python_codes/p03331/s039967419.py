N=input()
a=0
for i in range(len(N)):
    a+=int(N[i])
if int(N)<10:
    print(N)
elif a==1:
    print(10)
else:
    print(a)