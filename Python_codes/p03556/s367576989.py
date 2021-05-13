n = int(input())

i=0
while (n-i)**0.5 % 1 != 0:
    i+=1
print(n-i)
