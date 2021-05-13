a,b = map(int,input().split())

d = [["."]*100 for i in range(100)]

i = 0
j = 0
while b > 1:

    count = 0
    while count < 50 and b > 1:
        d[i][j] = "#"
        count += 1
        b -= 1
        j += 2
    i += 2
    j = 0

for i in range(50,100):
    for j in range(100):
        d[i][j] = "#"

i = 0
j = 0
while a > 1:

    count = 0
    while count < 50 and a > 1:
        d[-i-1][-1-j] = "."
        count += 1
        a -= 1
        j += 2
    i += 2
    j = 0
print(100,100)
for i in d:
    print(*i,sep="")