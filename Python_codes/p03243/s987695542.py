N = int(input())
for i in range(N, 1000):
    if str(i)[0] == str(i)[1] == str(i)[2]:
        print(i)
        break