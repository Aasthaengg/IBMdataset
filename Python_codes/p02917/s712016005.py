n = int(input())
b_list = list(map(int, input().split()))
b_list.append(b_list[-1])
a_list = [0] *n
a_list[0] = b_list[0]
for i in range(1,n):
    #print(i)
    if b_list[i-1] <= b_list[i]:
        a_list[i] = b_list[i-1]
    else:
        a_list[i] = b_list[i]
    #print(a_list)
print(sum(a_list))