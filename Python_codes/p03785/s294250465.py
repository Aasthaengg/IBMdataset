n, c, k = map(int,input().split())
tl = []
for i in range(n):
    tl.append(int(input()))
tl.sort()

if c == 1:
    print(n)
    exit()

end = tl[0] + k
passenger_cnt = 1
bus_cnt = 0
for i in range(1,n):
    # 間に合う場合
    if end >= tl[i]:
        passenger_cnt += 1
        if i == n-1:
            if passenger_cnt <= c:
                bus_cnt += 1
                break
            else:
                bus_cnt += 2
                break
        elif passenger_cnt == c:
            bus_cnt += 1
            passenger_cnt = 0
            end = tl[i+1]+k

    # 間に合わない場合
    else:
        if i == n-1:
            bus_cnt += 2
            break
        bus_cnt += 1
        end = tl[i] + k
        passenger_cnt = 1

print(bus_cnt)