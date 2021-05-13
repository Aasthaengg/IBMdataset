import sys
whi,bla=map(int,input().split())
if(bla==0):
    print("1 1")
    print(".")
    sys.exit()
elif(whi==0):
    print("1 1")
    print("#")
    sys.exit()



whi-=1
bla-=1

field=[]
while(whi//50 >0):
    field.append(["#."]*50)
    field.append(["#"]*100)
    whi-=50

field.append(["#."]*whi + ["##"]*(50-whi))
field.append(["#"]*100)
field.append(["."]*100)

while(bla//50 >0):
    field.append(["#."]*50)
    field.append(["."]*100)
    bla-=50

field.append(["#."]*bla +[".."]*(50-bla))

print("{} 100".format(len(field)))
for i in range(len(field)):
    print("".join(field[i]))