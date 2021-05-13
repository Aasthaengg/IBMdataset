n = int(input())
count = 0
while True:
    count += 1
    if n < 2**count:
        print(2**(count-1))
        break
