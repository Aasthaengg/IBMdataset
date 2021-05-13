N = int(input())
A = [input() for _ in range(N)]

n = 0
Acount, Bcount,both = 0,0,0
for a in A:
    n += a.count("AB")
    if (a[0]=="B")&(a[-1]=="A"):both+=1
    elif a[0] == "B":Bcount+=1
    elif a[-1] == "A":Acount+=1

# print(n,Acount,Bcount,both)
n += min(Acount,Bcount)
if Acount+Bcount>0:n += both
elif both>0:n += both-1
print(n)
