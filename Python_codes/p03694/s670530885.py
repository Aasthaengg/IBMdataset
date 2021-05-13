n = int(input())
a_list = list(map(int, input().split()))
a_list = list(set(a_list))
a_list.sort()
r = a_list[-1]-a_list[0]
print(r)