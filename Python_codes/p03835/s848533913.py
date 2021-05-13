count = 0
a,b = map(int,input().split())
for i in range(a+1):
    for j in range(a+1):
            z = b - i - j
            if 0<=z<=a:
                count +=1
print(count)