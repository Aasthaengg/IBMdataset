n = int(input())
a = 0
b = 0
for i in range(1, 10):
    b = i
    a = n // i
    if n % i !=0: continue
    elif a <= 9 and b <= 9:
        print('Yes')
        exit()
print('No')