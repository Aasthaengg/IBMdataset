S=input()
key="keyence"

if S.find(key)!=-1:
    print("YES")
    exit()


count=0
for i in range(7):
    s=S[i]
    if s==key[count]:
        count+=1
    else:
        break

for i in range(-1,-8,-1):
    s=S[i]
    if s==key[i]:
        count+=1
    else:
        break
if count>=7:
    print("YES")
else:
    print("NO")