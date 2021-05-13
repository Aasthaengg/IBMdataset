x,y = map(int,input().split())

count = y

for i in range(x-1):
    count *= y-1
print(count)