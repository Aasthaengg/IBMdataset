n = int(input())
flag = True
for _ in range(n):
    ai = int(input())
    if ai % 2 == 0:
        continue
    else:
        flag = False
if flag:
    print("second")
else:
    print("first")