n,k = map(int,input().split())
l_list = list(map(int,input().split()))
s_l_list = sorted(l_list,reverse = True)
ans_list = s_l_list[:k]
print(sum(ans_list))
