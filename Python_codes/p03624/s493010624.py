import string

s = list(input())
c = [chr(i) for i in range(97, 97+26)]
count = 0

for i in c:
    if i not in s:
        print(i)
        break
    else:
        count += 1

if count == 26:
    print("None")
else:
    pass
