def plass_only(a):
    for i in a:
        if i < 0:
            return 0
    return 1

def minus_only(a):
    for i in a:
        if i > 0:
            return 0
    return 1

def sarch(list, a):
    for i in range(len(list)):
        if a == list[i]:
            return i
            break

N = int(input())
a = list(map(int, input().split()))
if plass_only(a) == 1:
    for i in range(1, len(a)):
        a[i] += a[i - 1]
    print(len(a) - 1)
    for i in range(1, len(a)):
        print(i, i + 1)

elif minus_only(a) == 1:
    for i in range(len(a) - 2, -1, -1):
        a[i] += a[i + 1]
    print(len(a) - 1)
    for i in range(len(a), 1, -1):
        print(i, i - 1)

else:
    a_p = [i for i in a]
    a_m = [i for i in a]
    count_p = 0
    count_m = 0
    plass_print = []
    minus_print = []
    for i in range(len(a)):
        while a_p[i] < 0:
            a_p[i] += max(a_p)
            count_p += 1
            plass_print.append(str(sarch(a_p, max(a_p)) + 1) + " " + str(i + 1))
            if count_p > N: break
        while a_m[i] > 0:
            a_m[i] += min(a_m)
            count_m += 1
            minus_print.append(str(sarch(a_m, min(a_m)) + 1) + " " + str(i + 1))
            if count_m > N: break
    if count_p <= count_m:
        count = count_p
        a = a_p
        for i in range(1, len(a)):
            a[i] += a[i - 1]
            count += 1
        print(count)
        for i in plass_print:
            print(i)
        for i in range(1, len(a)):
            print(i, i + 1)

        
    else:
        count = count_m
        a = a_m
        for i in range(len(a) - 2, -1, -1):
            a[i] += a[i + 1]
            count += 1
        print(count)
        for i in minus_print:
            print(i)
        for i in range(len(a), 1, -1):
            print(i, i - 1)
        
