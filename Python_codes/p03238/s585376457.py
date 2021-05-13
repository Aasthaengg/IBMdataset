n = int(input())
if n == 2:
    ans = 0
    for i in range(2):
        ans += int(input())
    print(ans)
elif n == 1:
    print('Hello World')