sosu = [2]
A = 10 ** 9 + 7
N = int(input())
man = []
buriburi = 1
n = [0] * 1000

def prime(a):
    flag = 0
    m = a
    for i in range(2,m):
        if m % i == 0:
            flag = 1
            break
    if flag == 0:
        sosu.append(a)

for i in range(3,1001,2):
    prime(i)

for i in sosu:
    for j in range(N,1,-1):
        mod = j
        while mod % i == 0:
            n[i] += 1
            mod = mod // i

for i in n:
    if i != 0:
        buriburi *= i + 1

print(buriburi % A)
