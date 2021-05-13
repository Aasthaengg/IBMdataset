A, B, C = map(int, input().split())
k = int(input())

def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

a = A
b = B
c = C
ans = 0
if a < b < c:
    ans = 1

for i in range(3**k):
    a = A
    b = B
    c = C
    i3 = Base_10_to_n(i, 3).zfill(k)
    mem = 0
    Pick = []
    for j in range(k):
        if i3[j] == '0':
            a *= 2
        elif i3[j] == '1':
            b *= 2
        elif i3[j] == '2':
            c *= 2
#        print(a, b, c)
    if a < b < c:
        ans = 1
#        print('!!')
if ans:
    print('Yes')
else:
    print('No')