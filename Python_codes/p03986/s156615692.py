s = input()
snum = 0
ans = 0
for i in s:
    if(i=='S'):
        snum+=1
    elif(snum>=1 and i=='T'):
        snum -=1
        ans +=1
print(len(s)-2*ans)