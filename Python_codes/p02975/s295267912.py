# coding: utf-8
from collections import Counter
N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)
k = list(cnt.keys())
k.sort()
if len(k) == 1:
    if k[0] == 0:
        print("Yes")
    else:
        print("No")
    exit()
elif len(k) == 2:
    if cnt[k[0]] == N // 3 and N % 3 == 0:
        print("Yes")
    else:
        print("No")
    exit()
elif len(k) == 3:
    if cnt[k[0]] == cnt[k[1]] == cnt[k[2]] and k[0] ^ k[1] == k[2]:
        print("Yes")
    else:
        print("No")
    exit()
else:
    print("No")
    exit()