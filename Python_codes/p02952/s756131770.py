a = int(input())
total = 0

    
for i in range(1,a+1):
    if i<10 or 99<i<1000 or 9999<i<100000:
        total+=1

print(total)