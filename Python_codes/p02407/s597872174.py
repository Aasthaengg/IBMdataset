n = int(input())
a = input()
a_list = a.split(" ")
y = ""
for i in range(n):
    y += a_list[n - (i + 1)]
    if n - (i + 1) == 0:
        break
    y += " "
print(y)
