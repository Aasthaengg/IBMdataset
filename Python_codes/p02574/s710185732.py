import sys

def enum_div(n):
    ir=int(n**(0.5))+1
    ret=[]
    for i in range(1,ir):
        if n%i == 0:
            ret.append(i)
            if (i!= 1) & (i*i != n):
                ret.append(n//i)
    return ret

n=int(input())
ap=list(map(int,input().split()))
amin=min(ap)
amax=max(ap)

if amax==1:
    print("pairwise coprime")
    sys.exit()

if amin!=1:
    bp=enum_div(amin)+[amin]
#    bp.sort()
    bp=bp[1:]
    for bpi in bp:
        yn=""
        for ai in ap:
            if ai%bpi!=0:
                yn="coprime"
                break
        if yn=="":
            print("not coprime")
            sys.exit()

if n>=78500 :
    print("setwise coprime")
    sys.exit()

aa=[0]*(amax+1)
for ai in ap:
    aa[ai]+=1

#p=get_primenumber(amax)

#for pp in p:
for pp in range(2,amax+1):
    psum=sum(aa[pp: :pp])
#    print("pp:",pp,psum)
    if psum>=2:
            print("setwise coprime")
            sys.exit()
## max_13.txt ... max_16.txt : "setwise coprime"
print("pairwise coprime")
   
