N = int(input())
for n in range(100000):
    x = int(n*1.08)
    if N==x:
        print(n)
        exit()
    if x > N:
        break
print(':(')
