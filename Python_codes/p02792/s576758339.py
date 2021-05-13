
N = int(input())


cnt = {}
for i in range(1,N+1):
    N_str = str(i)

    num = N_str[0]+N_str[-1]
    if N_str[-1] == '0':
        pass
    else:
        if num in cnt.keys():
            cnt[num] +=1
        else:
            cnt[num] = 1

ans = 0
for i in cnt.keys():
    try:
        cnt_inv = cnt[i[::-1]]
        ans += cnt[i] * cnt_inv
    except:
        pass
print(ans)