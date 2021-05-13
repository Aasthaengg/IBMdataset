n = int(input())
a = list(map(int, input().split()))
x = 'Y'
num = -1
while x == 'Y':
    l = []
    num += 1
    for i in a:
        if i%2 == 0:
            l.append(i//2)
        else:
            x = 'N'
            break
    a = l
print(num)