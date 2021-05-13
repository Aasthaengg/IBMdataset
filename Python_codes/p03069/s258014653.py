n=int(input())
s=input()
s=s

ll=0 #左側の黒い数を保持
rr=s.count(".") #右側の白い数を保持

result=ll+rr
for item in s:
    if item=="#":
        ll+=1
    else:
        rr-=1
    
    result=min(result,ll+rr)

print(result)
