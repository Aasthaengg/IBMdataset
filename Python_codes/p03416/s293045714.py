def f(x):
    l = len(x)
    i = 0
    while x[i] == x[l-i-1]:
        i += 1
        if i > (l//2):
            return True
            break
    return False

A, B = map(int, input().split())
count = 0
for i in range(A, B+1):
    if f(str(i)):
        count += 1
print(count)
