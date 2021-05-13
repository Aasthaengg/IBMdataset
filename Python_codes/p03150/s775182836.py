s=input()
k="keyence"
if s.find(k,0,7)!=-1 or s.find(k,len(s)-7)!=-1:
    print("YES")  
    exit()
for i in range(1,7):
    a=s.find(k[:i],0,len(k[:i]))
    if a==0:
        b=s.find(k[i:],len(s)-len(k[i:]))
        if b!=-1:
            print("YES")
            exit()
print("NO")







