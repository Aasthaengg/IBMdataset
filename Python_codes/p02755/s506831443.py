A,B = map(int, input().split())

n = 0
while True:

    if int(n * 0.08) == A and int(n*0.1) == B:
        break

    n += 1

    if n > 10000:
        n = -1
        break

print(n)