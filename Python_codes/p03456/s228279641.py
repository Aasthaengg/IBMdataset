a,b = input().split()
c = int(a+b)

for i in range(100111):
    if i*i == c:
        print("Yes")
        exit()
    
print("No")

