from collections import Counter

N = int(input())
a = list(map(int, input().split()))

c = Counter(a)

if c[0] == N:
    print("Yes")
elif N%3 == 0 and len(c) == 2:
    for A in a:
        if c[A] == (2*N)//3:
            print("Yes")
            break
    else:
        print("No")
elif N%3 == 0 and len(c) == 3:
    tmp = list(set(a))
    if c[tmp[0]] == c[tmp[1]] == c[tmp[2]] and tmp[0] ^ tmp[1] ^ tmp[2] == 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")