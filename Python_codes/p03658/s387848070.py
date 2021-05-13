N, K = map(int, input().split())
lists = list(map(int, input().split()))
sort_list = sorted(lists, reverse=True)
print(sum(sort_list[0:K]))