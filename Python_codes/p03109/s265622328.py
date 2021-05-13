s=str(input())
ans="TBD"
if int(s[:4])>2019:
    ans="Heisei"
    
elif int(s[:4])==2019:
    if int(s[5:7])<=4:
        if int(s[8:])<=30:
            ans="Heisei"
print(ans)