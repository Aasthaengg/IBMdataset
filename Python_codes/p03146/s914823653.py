s = int(input())

a = s
ar = [a]
for i in range(1, 100000000):
    if(a % 2 == 0):
        a = a/2
    else:
        a = 3*a + 1
    if(ar.count(a) == 1):
        # print("a", a)
        print(i+1)
        break
    # print("a", a)
    ar.append(a)
