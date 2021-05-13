ip = int(input())

for i in range(1,11):
    pr = 1000 * i
    if int(pr) - ip >= 0:
        print(pr - ip)
        break

