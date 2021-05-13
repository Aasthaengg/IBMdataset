N = int(input())
for i in range(N, N + 111):
    if str(i).count(str(i)[0]) == 3:
        print(i)
        break
