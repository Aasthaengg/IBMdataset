n=int(input())
money=100000
for i in range(n):
    money*=1.05
    if money%1000==0:
        pass
    else: 
        money=int(money//1000*1000+1000)
    i+=1
print(money)
