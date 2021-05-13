S = list(input())
T = list(input())


def rolling(str, n):
    return str[n:len(str)] + str[:n]


for i in range(len(S)):
    if S == rolling(T, i):
        print("Yes")
        exit()

print("No")
