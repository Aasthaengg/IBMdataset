def existOdd(lst):
    for i in lst:
        if i%2==1:
            return False
    return True

cookie=list(map(int,input().split()))
seen=[]
res=0
while existOdd(cookie):
    seen.append(cookie)
    cookie=[cookie[1]/2+cookie[2]/2,cookie[0]/2+cookie[2]/2,cookie[0]/2+cookie[1]/2]
    if cookie in seen:
        res=-1
        break
    res+=1

print(res)
