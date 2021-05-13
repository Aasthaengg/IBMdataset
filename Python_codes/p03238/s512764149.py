N = int(input())

if N == 1:
    print('Hello World')
if N == 2:
    res = 0
    for _ in range(2):
        res += int(input())
    print(res)