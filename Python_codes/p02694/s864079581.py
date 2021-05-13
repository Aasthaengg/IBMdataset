a = 100
b = int(input())
d = 0
while b>a:
    a+=(a//100)
    d+=1
print(d)