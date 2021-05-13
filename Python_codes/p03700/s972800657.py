n,a,b=map(int,input().split())
h=[]
for _ in range(n):
    h.append(int(input()))

lo=0
hi=10**9
while lo<hi:
    md=(lo+hi)//2
    def chk(md):
        d=a-b
        cnt=0
        for i in h:
            i-=md*b
            if i>0:
                cnt+=i//d
                if i%d:
                    cnt+=1
        if cnt<=md:
            return True
        else:
            return False
    if chk(md):
        hi=md
    else:
        lo=md+1
print(lo)

