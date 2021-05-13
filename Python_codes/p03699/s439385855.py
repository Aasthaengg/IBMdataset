n = int(input())
sum = 0
s = []
for i in range(n) :
    x = int(input())
    sum += x
    if x%10 != 0 :
        s.append(x)


if sum %10 != 0 :
    print(sum)
    exit()

while len(s)>0 :
    m = min(s)
    sum -= m
    if sum%10 != 0 :
        print(sum)
        exit()

print(0)