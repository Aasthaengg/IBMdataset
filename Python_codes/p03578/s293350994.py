from collections import Counter

N = int(input())
D = Counter(list(map(int, input().split())))
M = int(input())
T = Counter(list(map(int, input().split())))

flag = True

for t, num in T.items():
    # print(t, num)
    if D[t] < num:
        flag = False
if flag:
    print("YES")
else:
    print("NO")
