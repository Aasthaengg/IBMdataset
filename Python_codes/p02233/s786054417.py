n = int(input())
data = []
x = []

if n == 0:
    print('1')
data.append(1)
if n == 1:
    print('1')
data.append(1)

if n >= 2:
    for i in range(2, n+1):
    #print(sum(data[i-2:i+1]))
    #print(data[1])
    #data.append(data[i])
        x = sum(data[i-2:i+1])
        data.append(x)
    #print(i, x)
        i = i + 1
    print(x)
