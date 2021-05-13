n = int(input())
res_list = []
for i in range(n):
    a,b=input().split()
    res_list.append((a,int(b)))
psorted_res_list = sorted(res_list, key=lambda x: x[1], reverse=True)
sorted_res_list = sorted(psorted_res_list, key=lambda x: x[0])
for i in range(n):
    print(res_list.index(sorted_res_list[i]) + 1)