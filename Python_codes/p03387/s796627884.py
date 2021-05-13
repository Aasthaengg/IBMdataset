a,b,c=sorted(map(int,input().split()))
#print(a,b,c)
cnt=0
if a%2==b%2==c%2:
    cnt=0
elif a%2==b%2:
    cnt+=1
    a+=1
    b+=1
elif b%2==c%2:
    cnt+=1
    b+=1
    c+=1
elif a%2==c%2:
    cnt+=1
    a+=1
    c+=1
#print(cnt,a,b,c)
cnt+=(c-a)//2+(c-b)//2
print(cnt)