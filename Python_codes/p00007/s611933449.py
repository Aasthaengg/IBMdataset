n=int(input())
s=100000

for i in range(n):
    s+=s*0.05
    if s%1000==0 :
        pass
    else:
        s=(s//1000+1)*1000
print(int(s))
