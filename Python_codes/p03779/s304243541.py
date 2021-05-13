X = int(input())
ans = 0

a_i = 0
n = 1
while a_i < X:
    a_i = a_i + n
    ans = n
    n += 1

print(ans)
