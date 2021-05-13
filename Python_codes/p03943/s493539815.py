abc = list(map(int, input().split()))
abc.sort(reverse=True)
print('Yes' if abc[0] - sum(abc[1:]) == 0 else 'No')