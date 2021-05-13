num_list = list(map(int,input().split()))
ans=0
ans=max(num_list[0]+num_list[1],num_list[0]-num_list[1],num_list[0]*num_list[1])
print(ans)