n = int(raw_input())
taro = 0
hanako = 0

for i in range(n):
    S = (raw_input()).split(" ")
    if (S[0] > S[1]):
        taro += 3
    elif (S[0] == S[1]):
        hanako += 1
        taro += 1
    else:
        hanako += 3

print str(taro) + " " + str(hanako)