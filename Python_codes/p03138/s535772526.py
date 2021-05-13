n,k=map(int,input().split())
a=list(map(int,input().split()))



#print(len(bin(10**12)))

cnt=[0]*len(str(bin(k))[2:])

#print(cnt)

for item in a:
    for j in range(min(len(str(bin(item))[2:]),len(str(bin(k))[2:]))):
        if item>>j &1:
            cnt[j]+=1

cnt=cnt[::-1]
result=0
for index,item in enumerate(cnt):
    #print(item)
    if item%2==0 and item==n//2:
        result+=0*(2**(len(cnt)-index-1))
    elif item<=n//2 and result+2**(len(cnt)-index-1)<=k:
        result+=2**(len(cnt)-index-1)
    else:
        result+=0*(2**(len(cnt)-index-1))
    #print(result)

ans=0
for item in a:
    #print(item,result,item^result)
    ans=ans+(item^result)
    #print(ans)
print(ans)





"""
001(1)
100(4)
101(5)

110(6)
100(4)
010(2)

011(3)
100(4)
111(7)
"""
