N = int(input())
count = 0
for i in range (10**9):
    count = i * i
    if count > N:
        print((i-1)*(i-1))
        break