n=int(input())
s=100000
for i in range (n):
    s*=1.05
    s=int(s)
    if s%1000==0:
        s=s
    else:
        s=(int(s/1000)+1)*1000

print(s)
