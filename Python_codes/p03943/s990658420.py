s = list(map(int, input().split()))
s_sort = sorted(s)
print('Yes' if s_sort[0]+s_sort[1] == s_sort[2] else 'No')