import math
n = input()
before = n[:int(len(n)/2)]
after = n[math.ceil(len(n)/2):]
after = after[::-1]

if after == before:
    print("Yes")
else:
    print("No")