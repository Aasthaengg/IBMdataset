I = input().split()
a = int(I[0])
b = int(I[1])
c = int(I[2])

cnt = 0
while a <= b:
    if c % a == 0:
        cnt += 1
    a += 1

print(str(cnt))