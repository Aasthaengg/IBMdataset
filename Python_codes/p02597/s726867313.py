N = int(input())
c = list(input())


l1 = list()
for i in range(N):
    if c[i] == 'R':
        l1.append(i)
        


num = 0

def swap(i, j):
    a = c[i]
    c[i] = c[j]
    c[j] = a
    return

if len(l1) >= 1:
    for i in range(N):
        if i > l1[-1]:
            break
        if c[i] == 'W':
             swap(i, l1.pop(-1))
             num += 1
        if len(l1) == 0:
            break
print(num)
