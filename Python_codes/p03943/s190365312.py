data = list(map(int, input().split()))
if max(data) == sum(data) - max(data):
    print("Yes")
else:
    print("No")
