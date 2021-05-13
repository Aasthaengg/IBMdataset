num = str(input())
a = num[0]
b = num[1]
c = num[2]
d = num[3]
plus = ["+", "+", "+"]
minus = ["-", "-", "-"]
for i in range(2**3):
    key = []
    for j in range(3):
        if ((i>>j) &1):
            key.append("+")
        else:
            key.append("-")
    ans = a + key[0] + b + key[1] + c + key[2] + d
    if eval(ans) == 7:
        print(ans + "=7")
        break
