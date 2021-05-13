n,k = map(int,input().split())
li = list(map(int,input().split()))

if k == 1:
    print(min(abs(max(li)),abs(min(li))))
    exit()

time_li = []
for i in range(n-k+1):
    #print(li[i:i+k]) [-30, -10, 10]
    tmp_time_li = []
    mi = li[i]
    ma = li[i+k-1]
    if mi > 0 and ma >0:
        tmp_time_li.append(ma)
    elif mi < 0 and ma < 0:
        tmp_time_li.append(abs(mi))
    else:
        orikaeshi = min(abs(mi),abs(ma))*2+max(abs(mi),abs(ma))
        tmp_time_li.append(orikaeshi)
    time_li.append(tmp_time_li[0])
print(min(time_li))