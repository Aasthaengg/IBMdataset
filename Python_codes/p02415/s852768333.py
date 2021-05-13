buf = input()
buf_len = len(buf)

str_array = []
for i in range(buf_len):
    str_array.append(buf[i])

for i in range(buf_len):
    if str_array[i].isupper():
        str_array[i] = str_array[i].lower()
    else:
        str_array[i] = str_array[i].upper()

for i in range(buf_len):
    print("%s" % str_array[i], end="")

print()

