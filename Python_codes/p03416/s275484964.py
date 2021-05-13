def is_palindromic(n):
    tmp = list(str(n))
    return tmp == tmp[::-1]


A, B = map(int, input().split())
count = 0
for i in range(A, B + 1):
    if is_palindromic(i):
        count += 1
print(count)
