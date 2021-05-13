N = int(input())
h_list = list(map(int, input().split()))


dp_list = [0, abs(h_list[0] - h_list[1])]
for n in range(2, N):
    h0 = h_list[n-2]
    h1 = h_list[n-1]
    h2 = h_list[n]
    tmp_min = min(abs(h2-h1)+dp_list[n-1], abs(h2-h0)+dp_list[n-2])
    dp_list.append(tmp_min)
print(dp_list[-1])
