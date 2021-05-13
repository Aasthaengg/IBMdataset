n = int(input())
x = n * 100 // 108

if int(x * 1.08) == n:
    print(x)
elif int((x+1) * 1.08) == n:
    print(x+1)
else:
    print(':(')
