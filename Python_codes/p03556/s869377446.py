N = int(input())
x = 0
while(1):
    if x*x > N:
        x -= 1
        break
    x += 1
        
print(x*x)