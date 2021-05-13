s = input()
n = 4

sum_val = 0
for i in range(1 << (n - 1)):
    val = int(s[0])
    expression = s[0]
    for j in range(n - 1):
        if (i >> j) & 1:
            val += int(s[j+1])
            expression += "+" + s[j+1]
        else:
            val -= int(s[j+1])
            expression += "-" + s[j+1]
    if val == 7:
        print(expression + "=7")
        quit()
