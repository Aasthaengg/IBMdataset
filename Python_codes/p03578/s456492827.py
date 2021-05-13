import collections
N = int(input())
D_list = [int(e) for e in input().split()]
M = int(input())
T_list = [int(e) for e in input().split()]
D_counted = collections.Counter(D_list)
T_counted = collections.Counter(T_list)

for difficult,count in T_counted.items():
    if difficult in D_counted and D_counted[difficult] >= count:
        pass
    else:
        print("NO")
        break
else:
    print("YES")