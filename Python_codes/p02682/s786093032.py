a,b,c,k = map(int,input().split())

if a>=k:
    m=k
elif a+b>=k:
    m=a
else:
    m=a-(k-a-b)

print(m)
