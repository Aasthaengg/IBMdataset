N = int(input())
count = 0
for i in range(1,6):
    if N >= 10**i:
        if i%2==1:
            count+=9*(10**(i-1))
    else:
        if i%2==1:
            count+=N-10**(i-1)+1
        break 
print(count)