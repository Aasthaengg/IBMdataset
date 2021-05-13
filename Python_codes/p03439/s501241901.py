N = int(input())
print(0,flush=True)
s = input().strip()
if s[0]!="V":
    x = s[0]
    low = 0
    high = N
    while high-low>1:
        mid = (high+low)//2
        print(mid,flush=True)
        s = input().strip()
        if s[0]=="V":
            break
        elif mid%2==0 and s[0]==x:
            low = mid
        elif mid%2==0 and s[0]!=x:
            high = mid
        elif mid%2==1 and s[0]==x:
            high = mid
        elif mid%2==1 and s[0]!=x:
            low = mid