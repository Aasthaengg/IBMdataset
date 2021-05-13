K = int(input())
#a1= 7 mod K
#a2= a1*10+7 mod K
#a3= a2*10+7 mod K
a = 0
count = -1
for i in range(K):
    a = (7 + a*10) % K
    if a  == 0:
        count=i+1
        break
print(count)