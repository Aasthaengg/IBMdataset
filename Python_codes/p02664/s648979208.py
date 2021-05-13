T = list(input())

for i in range(len(T)):
    if T[i] == "?":
        if i == len(T) - 1:
            T[i] = "D"
        else:
            if i > 0 and T[i - 1] == "P":
                T[i] = "D"
            elif T[i + 1] == "D" or T[i + 1] == "?":
                T[i] = "P"
            else:
                T[i] = "D"

print("".join(T))