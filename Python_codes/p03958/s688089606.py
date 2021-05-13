num_cakes, num_kinds = map(int,input().split())
kinds_ls = list(map(int, input().split()))
kinds_ls.sort()
max_value = kinds_ls[-1] - 1
else_sum = sum(kinds_ls[:num_kinds-1])

print(max(max_value-else_sum,0))
