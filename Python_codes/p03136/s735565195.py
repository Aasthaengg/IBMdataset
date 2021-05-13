N = int(input())
L = sorted(list(map(int, input().split())))
last = L.pop(N - 1)
if last < sum(L):
    print("Yes")
else:
    print("No")
