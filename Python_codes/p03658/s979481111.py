n,k = map(int,input().split())
l_list = list(map(int,input().split()))
l_list.sort(reverse=1)
print(sum(l_list[0:k]))