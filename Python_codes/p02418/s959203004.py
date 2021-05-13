wor = raw_input()
word = raw_input()
a = [[wor]for i in range(10)]
b = ""
for i in a:
    b = b + "".join(i)


if b.count(word) > 0:
    print("Yes")
else:
    print("No")