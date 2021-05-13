N = int(input())
A = list(map(int,input().split()))
check = []
every = 0

for a in A:
    if a < 400:
        check.append(1)
    elif a < 800:
        check.append(2)
    elif a < 1200:
        check.append(3)
    elif a < 1600:
        check.append(4)
    elif a < 2000:
        check.append(5)
    elif a < 2400:
        check.append(6)
    elif a < 2800:
        check.append(7)
    elif a < 3200:
        check.append(8)
    else:
        every += 1
length = len(set(check))
if length == 0:
    length = 1
    every -= 1

print(length,length+every)