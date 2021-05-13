lst = sorted(list(map(int, input().split())), reverse=True)
k = int(input())
print(lst[0] * (2 ** k) + sum(lst[1:]))