from collections import Counter

n = int(input())
D = Counter([int(i) for i in input().split()])
m = int(input())
T = Counter([int(i) for i in input().split()])

for k, v in T.items():
    if k not in D.keys():
        print("NO")

        quit()
    else:
        if D[k] < T[k]:
            print("NO")
            quit()
        else:
            continue

print("YES")
