# ???
n,a,b,c,d=map(int,input().split())
s=input()
ans="Yes"

if c<d:
    btod=s[b:d]
    atoc=s[a:c]
    if btod.count("##")>0:ans="No"
    if atoc.count("##")>0:ans="No"
else:
    btod=s[b-1-1:d+1]
    atoc=s[a:c]
    if atoc.count("##")>0:ans="No"
    else:
        if btod.count("...")==0:ans="No"
    
print(ans)
