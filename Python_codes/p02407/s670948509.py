n = int(input())
l = list(map(int, input().split()))
l.reverse()
s = ''
for i in range(n):
    if i >= 1:
        print(' ', end='')
    print(l[i], end='')
print()

