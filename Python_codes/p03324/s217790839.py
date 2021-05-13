s = input().split()

d = int(s[0])
n = int(s[1])

answer = 0

if d == 0:
    if n == 100:
        answer = 101
    else:    
        answer = n
elif d == 1:
    if n == 100:
        answer = 10100
    else:
        answer = 100 * n
elif d == 2:
    if n == 100:
        answer = 1010000
    else:
        answer = 10000 * n

print(answer)