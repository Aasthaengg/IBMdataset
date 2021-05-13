N=int(input())
#75=5*5*3=25*3=15*5=75*1
#100!=9.3*10^157
#2^74=1.8*10^12,3^74=...,140^74=
#つまり,4こ-4こ-2こ、24こ-2こ、14こ-4こ,74こ
#となる組み合わせの探査になる?
insuu=[0]*(100+1)
l=[]
sevenfour=0
twofour=0
onefour=0
four=0
two=0
for k in range(N):
    pf = {}
    m = k+1
    for i in range(2, int(m ** 0.5) + 1):
        while m % i == 0:
            pf[i] = pf.get(i, 0) + 1
            m //= i
    if m > 1: pf[m] = 1
    #print(pf)
    keys = list(pf.keys())
    values = list(pf.values())
    for i in range(len(keys)):
        insuu[keys[i]]=insuu[keys[i]]+values[i]
    # print(l)	#これでlistになった
#print(insuu)
for i in range(101):
    if insuu[i]>=74:
        sevenfour = sevenfour+1
    if insuu[i]>=14:
        onefour=onefour+1
    if insuu[i]>=24:
        twofour=twofour+1
    if insuu[i]>=4:
        four=four+1
    if insuu[i]>=2:
        two=two+1
print(((four*(four-1))//2)*(two-2)+twofour*(two-1)+onefour*(four-1)+sevenfour)