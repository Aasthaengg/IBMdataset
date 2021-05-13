A = input().split()
N = []

for i in A:
    if i.isdigit():
        N.append(i)
    elif str(i) == '+':
        t1 = N.pop()
        t2 = N.pop()
        t3 = int(t2) + int(t1)
        N.append(t3)
    elif str(i) == '*':
        t1 = N.pop()
        t2 = N.pop()
        t3 = int(t2) * int(t1)
        N.append(t3)
    else:
        t1 = N.pop()
        t2 = N.pop()
        t3 = int(t2) - int(t1)
        N.append(t3)

print(N.pop())