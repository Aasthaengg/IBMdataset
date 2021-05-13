h = int(input())

num = 1
count = 0
while h > 0:
    h = h//2
    count += num
    num = num*2
print(count)