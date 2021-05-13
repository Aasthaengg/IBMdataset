from collections import defaultdict
from sys import exit

H, W = map(int, input().split())
char_counter = defaultdict(int)

for _ in range(H):
    for s in input():
        char_counter[s] += 1

if H % 2 == 0 and W % 2 == 0:
    for k, v in char_counter.items():
        if v % 4 != 0:
            print("No")
            exit()
    print("Yes")
elif H % 2 == 0 and W % 2 == 1:
    holder = defaultdict(int)
    counter = 0
    for k, v in char_counter.items():
        if v % 4 != 0:
            for _ in range(v % 4):
                holder[k] += 1
                counter += 1
    if counter <= H:
        for kk, vv in holder.items():
            if vv % 2 != 0:
                print("No")
                exit()
        print("Yes")
    else:
        print("No")
elif H % 2 == 1 and W % 2 == 0:
    holder = defaultdict(int)
    counter = 0
    for k, v in char_counter.items():
        if v % 4 != 0:
            for _ in range(v % 4):
                holder[k] += 1
                counter += 1
    if counter <= W:
        for kk, vv in holder.items():
            if vv % 2 != 0:
                print("No")
                exit()
        print("Yes")
    else:
        print("No")
elif H % 2 == 1 and W % 2 == 1:
    holder = defaultdict(int)
    counter = 0
    for k, v in char_counter.items():
        if v % 4 != 0:
            for _ in range(v % 4):
                holder[k] += 1
                counter += 1
    if counter <= W + H - 1:
        no_odd = False
        for kk, vv in holder.items():
            if vv % 2 != 0:
                if no_odd:
                    print("No")
                    exit()
                else:
                    no_odd = True
        print("Yes")
    else:
        print("No")
