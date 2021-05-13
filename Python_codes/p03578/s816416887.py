import collections
N = int(input())
D = list(map(int,input().split()))
M = int(input())
T = list(map(int,input().split()))
D_1 = collections.Counter(D)
T_1 = collections.Counter(T)
for i in set(T):
    if D_1[i] < T_1[i]:
        print("NO")
        exit()
print("YES")