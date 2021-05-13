s = input()
A = [int(s[0]), int(s[1]), int(s[2]), int(s[3])]

for i in range(8):
    b = format(i, "03b")
    S = A[0]
    for j in range(3):
        if b[j] == "0":
            S += A[j + 1]
        else:
            S -= A[j + 1]
    if S == 7:
        break

op = ["+", "-"]
ans = s[0] + op[int(b[0])] + s[1] + op[int(b[1])] + s[2] + op[int(b[2])] + s[3] + "=7"
print(ans)