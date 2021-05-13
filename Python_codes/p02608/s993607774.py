N = int(input())
list = []
for i in range(10100):
    list.append(0)

for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            n = x*x + y*y + z*z + x*y + y*z +z*x
            if n <= 10000:
                list[n] += 1
                
for i in range(N):                
    print(list[i+1])