n = int(input())
L = list(map(int,input().split()))
L = sorted(L)
s = sum(L[:n-1])
if L[-1] < s:
    print("Yes")
else:
    print("No")