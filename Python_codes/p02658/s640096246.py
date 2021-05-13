n = int(input())
list_a = [int(x) for x in input().split()]
list_a_str = [str(s) for s in list_a]
ans = 1

for i in range(0, n):
    if list_a_str[i] in '0':
        print('0')
        exit()

for i in range(0, n):
    ans *= list_a[i]
    if ans > 10 ** 18:
        print('-1')
        exit()

else: print(ans)