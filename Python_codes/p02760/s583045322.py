import itertools
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
a3 = list(map(int, input().split()))
a = list(itertools.chain.from_iterable([a1, a2, a3]))

n = int(input())
b = [int(input()) for _ in range(n)]

for i in b:
    a = [x if x != i else 0 for x in a]

if a[0] == 0 and a[1] == 0 and a[2] == 0:
    print("Yes")
elif a[3] == 0 and a[4] == 0 and a[5] == 0:
    print("Yes")
elif a[6] == 0 and a[7] == 0 and a[8] == 0:
    print("Yes")
elif a[0] == 0 and a[3] == 0 and a[6] == 0:
    print("Yes")
elif a[1] == 0 and a[4] == 0 and a[7] == 0:
    print("Yes")
elif a[2] == 0 and a[5] == 0 and a[8] == 0:
    print("Yes")
elif a[0] == 0 and a[4] == 0 and a[8] == 0:
    print("Yes")
elif a[2] == 0 and a[4] == 0 and a[6] == 0:
    print("Yes")
else:
    print("No")
