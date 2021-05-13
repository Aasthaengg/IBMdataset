e = list(input())
t = list(input())
password = ""
count_e = 0
count_t = 0
for i in range(len(e) + len(t)):
    if i % 2 == 0:
        password += e[count_e]
        count_e += 1
    else:
        password += t[count_t]
        count_t += 1
print(password)
