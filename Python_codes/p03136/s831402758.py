N = int(input())
list = list(map(int, input().split()))
print("Yes" if 2*max(list) < sum(list) else "No")