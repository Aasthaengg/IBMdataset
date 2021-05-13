N = int(input())
seats = [""] * N

# 準備
print(0)
seats[0] = input()
if seats[0] == "Vacant":
    exit()
print(N - 1)
seats[N - 1] = input()
if seats[N - 1] == "Vacant":
    exit()

l = 0
r = N - 1
while True:
    m = (l + r) // 2
    print(m)

    s = input()
    if s == "Vacant":
        exit()
    seats[m] = s

    if (seats[l] == seats[m]) & ((m - l) % 2 == 1):
        r = m
    elif (seats[l] != seats[m]) & ((m-l) % 2 == 0):
        r = m
    else:
        l = m



