N = int(input())
a = N // 100
b = N % 10
c = N // 10
d = c % 10
if a ==7 or b == 7 or d ==7:
    print('Yes')
else:
    print('No')