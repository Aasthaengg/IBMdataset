count = 0
x = raw_input().split()
for i in range(int(x[0]),int(x[1])+1):
    if int(x[2]) % i ==0:
       
        count += 1
print count