s=input()
if s=="AKIHABARA":
    print("YES")
else:
    ans="YES"
    if len(s)>=9 or "KIH" not in s:
        ans="NO"
    else:
        t=s.replace("A","")
        if t!="KIHBR":
            ans="NO"
        else:
            k,b,r=s.find("K"),s.find("B"),s.find("R")
            if k>1 or b-k>4 or r-b>2:
                ans="NO"
    print(ans)