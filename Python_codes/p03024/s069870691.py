s=input()
win=0
for i in s:
    if i=="o":
        win+=1
if win+15-len(s)>=8:
    print("YES")
else:
    print("NO")



        
