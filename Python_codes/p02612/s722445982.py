n = int(input())
for i in range(1,11):
    if 1000 * i >= n:
        print(1000*i-n)
        break