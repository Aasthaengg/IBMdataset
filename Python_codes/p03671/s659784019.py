num_lists = list(map(int, input().split()))

num_lists.sort()
ans = num_lists[0] + num_lists[1]

print(ans)