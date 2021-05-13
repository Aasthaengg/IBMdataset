S = input()
A = "".join(list(reversed(S)))
i = 0

while i != len(S):
    if A[i:i+5] == "maerd":
        i += 5
    elif A[i:i+5] == "esare":
        i += 5
    elif A[i:i+7] == "remaerd":
        i += 7
    elif A[i:i+6] == "resare":
        i += 6
    else:
        print("NO")
        exit()
print("YES")