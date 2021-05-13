n=int(input())
l =list(map(int, input().split()))
M = max(l)
L = sum(l)-M
if L > M:
    print("Yes")
else:
    print("No")