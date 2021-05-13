n, k = map(int, input().split())
s = str(input())
for i in range(n):
    if i + 1 == k:
        if s[i] == 'A':
            print('a', end='')
        elif s[i] == 'B':
            print('b', end='')
        else:
            print('c', end='')
    else:
        print(s[i], end='')