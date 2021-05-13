n = int(input())

result = 0
for i in range(1, int(n**(1/2)+1)):
    if n%i==0:
        x = n//i -1
        if x > i:
            result += x
print(result)