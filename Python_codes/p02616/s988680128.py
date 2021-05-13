def make_set_list(array,valid):
    new_array = []
    for i in range(len(array)//2):
        new_array.append(array[2*i]*array[2*i+1])
    if len(array)%2 == 1 and valid == 1:
        new_array.append(array[len(array)-1])
    return new_array

N, K = list(map(int,input().split()))
As = list(map(int,input().split()))
p_nums = []
n_nums = []
for i in range(N):
    n = As[i]
    if n < 0:
        n_nums.append(n)
    else:
        p_nums.append(n)
As.sort(key = abs)
n_nums.sort()
p_nums.sort(reverse = True)
if len(p_nums) > 0:
    if N > K:
        ok = True
    elif len(n_nums) % 2 == 0:
        ok = True
    else:
        ok = False
elif K % 2 == 0:
    ok = True
else:
    ok = False

ans = 1

if ok:
    if K % 2 == 0:
        set_p_num = make_set_list(p_nums,1)
        set_n_num = make_set_list(n_nums,0)
        set_num = set_p_num + set_n_num
        set_num.sort(reverse = True)
        for i in range(K//2):
            ans = (ans*(set_num[i]%(10**9+7)))%(10**9+7)
    else:
        ans = p_nums.pop(0)
        set_p_num = make_set_list(p_nums,1)
        set_n_num = make_set_list(n_nums,0)
        set_num = set_p_num + set_n_num
        set_num.sort(reverse = True)
        for i in range(K//2):
            ans = (ans*(set_num[i]%(10**9+7)))%(10**9+7)
else:
    for i in range(K):
        ans = (ans*(As[i]%(10**9+7)))%(10**9+7)

print(ans)
