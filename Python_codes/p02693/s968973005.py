k = int(input())
a, b = map(int, input().split())

for i in range(b-a+1):
    if (a+i) % k == 0:
        print('OK')
        break
    elif a+i == b:
        print('NG')