n, k = [int(x) for x in input().split()]
v_list = [int(x) for x in input().split()]

stop = min(n, k)

ans = 0
for a in range(stop + 1):
    a_list = v_list[:a]
    for b in range(stop + 1 - a):
        b_list = v_list[n-b:]
    
        temp_list = a_list + b_list
        temp_list.sort(reverse=True)

        for _ in range(k - a - b):
            if len(temp_list) == 0 or temp_list[-1] >= 0:
                break
            temp_list.pop()

        temp = sum(temp_list)
        if ans < temp:
            ans = temp
print(ans)