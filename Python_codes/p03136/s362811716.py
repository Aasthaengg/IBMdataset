n = int(input())
L = list(map(int, input().split()))

max_length = max(L)

if max_length < sum(L) - max_length:
    print("Yes")
else:
    print("No")