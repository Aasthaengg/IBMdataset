W=input().upper()
T=""
while True:
    Ti = input()+" "
    if Ti != "END_OF_TEXT ":
        T+= Ti.upper()
    else:
        break
TT=T.split(" ")
c=0
for t in TT:
    if t == W:
        c+=1
print(c)