s = input()

oddstring = s[0]
a = ((len(s) + 1) // 2) - 1

if a > 0:
    for i in range(a):
        oddstring += s[2*i+2]

print(oddstring)
