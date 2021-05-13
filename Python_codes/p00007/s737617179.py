num=int(input())
debt=100000
for i in range(1,num+1):
    debt+=((debt)/100)*5
    if not debt%1000==0:
        debt-=(debt%1000)
        debt+=1000
print(int(debt))