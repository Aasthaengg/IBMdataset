a,b = map(int, input().split())

count = 0
for i in range(1,a+1):
    if int(str(i)+str(i)) <= int(str(a)+str(b)):
        count += 1

print(count)