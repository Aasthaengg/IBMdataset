from math import sqrt
n = int(input())
a = 1+8*n
b = int(sqrt(a))
if b**2 != a or b%2==0:
    print("No")
    exit()
else:
    k = (1 + b)//2
    s = [[] for i in range(k)]
    cur = 1
    for i in range(k):
        for j in range(k-i-1):
            s[i].append(cur)
            s[i+j+1].append(cur)
            cur += 1
    print("Yes")
    print(k)
    for i in range(k):
        res = "{} ".format(len(s[i])) + " ".join(map(str, s[i]))
        print(res)