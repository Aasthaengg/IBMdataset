n = int(input())
b = list(map(int , input().split()))

def f(c):
    for i in reversed(range(len(c))):
        if c[i] == i+1:
            return (c[i], c[:i] + c[i+1:])
    return (-1, c)

ans = []
for i in range(n):
    (a, b) = f(b)
    if a == -1:
        print(-1)
        exit()
    ans.append(a)
    #print(ans, b)

print('\n'.join(map(str, reversed(ans))))
