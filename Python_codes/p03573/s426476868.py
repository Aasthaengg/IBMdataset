a, b, c = map(int, input().split())
lst = sorted([a, b, c])

for i in range(2):
    if lst[i] == lst[i+1]:
        print(sum(lst) - 2*lst[i])