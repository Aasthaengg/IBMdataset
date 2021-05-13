tmp = input().split(" ")
a = int(tmp[0])
b = int(tmp[1])
t = int(tmp[2])

sum = 0
for i in range(1, t+1):
    if(i % a == 0):
       sum += b

print(sum)
