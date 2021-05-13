n=int(input())
pro=1
for i in range(1,n+1):
    pro=(pro*(i))%1000000007
print(pro)