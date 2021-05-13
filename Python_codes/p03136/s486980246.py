N = int(input())
L = list(map(int,input().split()))
s = 0
for i in L:
    s += i
s -= max(L)
if max(L) < s:
    print("Yes")
else:
    print("No")