N = int(input())

cnt = 0

N4 = int(N /1000)

N = N - N4 * 1000

N3 = int(N /100)


N = N - N3 * 100

N2 = int(N /10)

N = N - N2 * 10
     

if N == 2:
    cnt =cnt + 1

if N4 == 2:
    cnt =cnt + 1

if N3 == 2:
    cnt =cnt + 1

if N2 == 2:
    cnt =cnt + 1

print(cnt)
