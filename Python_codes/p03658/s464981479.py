n, k = map(int, input().split())
l_list = list(map(int, input().split()))
l_list.sort(reverse=True)
r_list = l_list[0:k]
print(sum(r_list))