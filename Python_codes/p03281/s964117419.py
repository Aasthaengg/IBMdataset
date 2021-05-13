n=input()

s=0
yakusu=0



for i in range(1,int(n)+1):
    s=0
    if i%2!=0:
        for k in range(1,i+1):
            if i%k==0:
                s+=1    
    if s==8:
        yakusu+=1         

print(yakusu)