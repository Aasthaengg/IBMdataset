N = int(input())
A_list = [int(e) for e in input().split()]
B_list = [int(e) for e in input().split()]

#B-Aで過剰/不足を取得
#過剰を並び替え、大きいものから不足に割り当てていく

shortage_list = list()
surplus_list = list()

for i in range(N):
    C = B_list[i]-A_list[i]
    if C > 0:
        shortage_list.append(C)
    elif C < 0:
        surplus_list.append(-C)
        
if sum(surplus_list) < sum(shortage_list):
    print(-1)
elif len(shortage_list) == 0:
    print(0)
else:
    surplus_list.sort(reverse=True)
    sum_shortage = sum(shortage_list)
    for i in range(len(surplus_list)):
        sum_shortage -= surplus_list[i]
        if sum_shortage <= 0:
            print(i + 1 + len(shortage_list))
            break