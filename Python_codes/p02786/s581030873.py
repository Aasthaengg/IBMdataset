H = int(input())

pw = 1
cnt = 0
while True:
    pw *= 2
    if pw > H:
        break
    cnt += 1

print(pw - 1)