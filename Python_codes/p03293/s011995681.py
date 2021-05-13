def rolling(str, n):
    return str[n:len(str)] + str[:n]


S = input()
T = input()
for i in range(len(S)):
    if rolling(S, i) == T:
        print("Yes")
        exit()

print("No")
