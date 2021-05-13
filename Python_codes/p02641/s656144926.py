X, N = map(int, input().split())

if N != 0:
    p_list = list(map(int, input().split()))
    p_list_min = sorted(p_list)
    
non_p_list = []

if N >= 1:
    for i in range(p_list_min[0]-1, p_list_min[-1]+2):
        if i not in p_list_min:
            non_p_list.append(i)
            ans_diff = abs(X - non_p_list[-1])+1
        for i in range(len(non_p_list)):
            temp_diff = abs(X - non_p_list[i])
            if ans_diff > temp_diff:
                ans_diff = temp_diff
                ans = non_p_list[i]
    #print(non_p_list)
    print(ans)
else:
    print(X)