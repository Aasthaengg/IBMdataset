n = int(input())

lis = list(map(int, input().split()))

lis = sorted(lis)

m = max(lis)

oth = sum(lis[:n-1])

if m < oth:
    print("Yes")
else:
    print("No")