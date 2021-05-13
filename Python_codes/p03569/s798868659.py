s = input()
n = len(s)
check_ls = []
for i in range(n):
    if s[i] != 'x':
        check_ls.append(s[i])
n_check = len(check_ls)
is_kaibun = True
for i in range(n_check//2):
    if check_ls[i] != check_ls[-i-1]:
        is_kaibun = False
if not is_kaibun:
    print(-1)
else:
    num_target = -(-n_check//2)
    not_x_count = 0
    for i in range(n):
        if s[i] != 'x':
            not_x_count += 1
        if not_x_count == num_target:
            center_ind = i
            break
    ans = 0
    #if n_check % 2 ==0:
        #right = center_ind+1
        #left = center_ind
    right = n-1
    left = 0
    while right > left:
        if s[right] == 'x' and s[left] != 'x':
            ans += 1
            left -= 1
        elif s[right] != 'x' and s[left] == 'x':
            ans += 1
            right += 1
        right -= 1
        left += 1
    print(ans)