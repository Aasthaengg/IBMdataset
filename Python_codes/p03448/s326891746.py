a = int(input())
b = int(input())
c = int(input())
x = int(input())
num = 0
if 500*a <= x:
    for i in range(a+1):
        for h in range(b+1):
            for j in range(c+1):
                if 500*i+100*h+50*j == x:
                    num += 1
else:
    for i in range((x//500)+1):
        for h in range(b+1):
            for j in range(c+1):
                if 500*i+100*h+50*j == x:
                    num += 1
print(num)