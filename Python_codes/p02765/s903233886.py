N,R=[int(i) for i in input().split()]
if N>=10:
    res=R
else:
    res=R+100*(10-N)
print(res)
