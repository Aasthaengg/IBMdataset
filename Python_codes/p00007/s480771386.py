n=int(input())
m=100000
for i in range(n):
    m=m*1.05
    if m % 1000 != 0 : 
        m=m-(m%1000)+1000
print(int(m))
