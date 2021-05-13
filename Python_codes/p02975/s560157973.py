import sys
input = sys.stdin.readline

N = int(input())
a = [int(i) for i in input().split()]

from collections import Counter

Count_a = Counter(a)

if len(Count_a) == 1:
    if Count_a[0] == N:
        print("Yes")
    else:
        print("No")

elif len(Count_a) == 2 and N % 3 == 0:
    if Count_a[0] == N // 3:
        print("Yes")
    else:
        print("No")

elif len(Count_a) == 3 and N % 3 == 0:
    three = list(set(a))
    if three[0] ^ three[1] ^ three[2] == 0:
        for i in range(3):
            if Count_a[three[i]] != N // 3:
                print("No")
                exit()
        print("Yes")
    else:
        print("No")

else:
    print("No")