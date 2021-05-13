n, a, b = map(int,input().split())

ans_list = []
for i in range(1,n+1):
    num_list = map(int,list(str(i)))
    if a<=sum(num_list)<= b:
        ans_list.append(i)

print(sum(ans_list))