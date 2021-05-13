n = int(input())
x = 0
c = True
for i in range(1000000):
    x = ((x *10) +7)%n
    if x == 0:
        print(i+1)
        c = False
        break
        
if c:
    print(-1)