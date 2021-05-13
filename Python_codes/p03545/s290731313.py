s = input()
a=int(s[0])
b=int(s[1])
c=int(s[2])
d=int(s[3])
for j in range(2):
    for k in range(2):
        for l in range(2):
            sm=a
            if j==0:
                B='+'
                sm+=b
            else:
                B='-'
                sm-=b
            if k==0:
                C='+'
                sm+=c
            else:
                C='-'
                sm-=c
            if l==0:
                D='+'
                sm+=d
            else:
                D='-'
                sm-=d
            if sm==7:
                
                m=str(a)+B+str(b)+C+str(c)+D+str(d)+'=7'
                print(m)
                exit()
