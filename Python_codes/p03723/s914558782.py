a, b, c = map(int, input().split())
count = 0
for i in range(1100):
    if (a%2 + b%2 + c%2):
        break
    d,e,f = (b+c)//2, (c+a)//2, (a+b)//2
    a,b,c = d,e,f
    count += 1
if(count>1000):
    count = -1
print(count)