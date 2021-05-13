N = int(input())
a = list(map(int, input().split()))
num = list(set(a))

if len(num) == 1 and num[0] == 0:
    print('Yes')
elif N % 3 == 0:
    if len(num) == 3:
        s = a.count(num[0])
        t = a.count(num[1])
        u = a.count(num[2])
        if s == t and t == u and u == s and num[0] ^ num[1] == num[2]:
            print('Yes')
        else:
            print('No')
    elif len(num) == 2:
        if a.count(max(num)) == a.count(0) * 2:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
else:
    print('No')
