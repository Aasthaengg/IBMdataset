#coding: UTF-8

buf = list(str(input()))
for i in range(len(buf)):
    if buf[i].isupper() == True:
        buf[i] = buf[i].lower()
        buf_changed = "".join(buf)
    elif buf[i].islower() == True:
        buf[i] = buf[i].upper()
        buf_changed = "".join(buf)

print(buf_changed)
