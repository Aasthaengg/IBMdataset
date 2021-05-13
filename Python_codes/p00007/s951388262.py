n = input()
a = 100000
for i in range(1,int(n)+1):
    a = int(a*1.05)
    if(a%1000 > 0):
        a = 1000*int(a/1000) + 1000

print(a)