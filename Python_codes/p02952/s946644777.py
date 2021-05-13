def count(n):
    c = 1
    while(n>=10):
        n = n//10
        c += 1
    return c
s = 0
n = int(input()) 
x = count(n)-1
for i in range(0,x,+2):
    s += 9*(10**i)
if (x+1) % 2:
    s += n-pow(10,x)+1
print(s)