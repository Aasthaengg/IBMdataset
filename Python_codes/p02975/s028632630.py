from collections import Counter

n = int(input())
a = list(map(int, input().split()))
ca = Counter(a)

if 0 in ca and ca[0] == n:
    print("Yes")
elif n % 3 == 0 and 0 in ca and ca[0] == n // 3 and len(ca) == 2:
    print("Yes")
elif n % 3 == 0 and len(ca) == 3:
    values = []
    for c in ca:
        if ca[c] == n // 3:
            values.append(c)
    
    if len(values) != 3:
        print("No")
    else:
        ans = 0
        for k in values:
            ans ^= k
        if ans == 0:
            print("Yes")
        else:
            print("No")
else:
    print("No")