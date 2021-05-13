l = input()
MOD = 10**9 + 7
r = len(l)
res = 0
num=0
for i in range(len(l)):
    tmp = r-i-1
    if(l[i]=="1"):
        res += pow(2,num,MOD) * pow(3,tmp,MOD)
        res%=MOD
        num+=1

res += pow(2,num)
print(res%MOD)
