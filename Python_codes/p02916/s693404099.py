n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

sum = 0
hantei = 0


for i in range(len(a)):


    if i == 0:
        sum = sum + b[a[i]-1]
        hantei = a[i]
    else:
        if a[i] == hantei + 1:
            sum = sum + b[a[i]-1] + c[a[i]-2]
            hantei = a[i]
        else:
            sum = sum + b[a[i]-1]
            hantei = a[i]
    
print(sum)