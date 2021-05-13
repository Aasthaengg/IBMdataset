s = str(input())
k = int(input())
count = 0
for i in s:
    if i == "1":
        count += 1
        if count == len(s):
            print(1)
            break
        else:
            pass
    else:
        if k <= count:
            print(1)
            break
        else:
            print(i)
            break
