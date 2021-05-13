n = int(input())

for v in range(int(n//1.08)+2):
    if int(v*1.08) == n:
        print(v)
        exit()
print(':(')