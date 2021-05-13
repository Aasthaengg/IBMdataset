n ,k = list(map(int, input().split()))
p_list = list(map(int,input().split()))

p_list.sort()
ans = sum(p_list[0:k])
print(ans)