n = int(input())

a = 100000

for i in range(n):
        a = a+a*0.05
    
        if a%1000 !=0:
            a = int(((a//1000)+1)*1000)
print(a)
