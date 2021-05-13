n = int(input())
l_ls = list(map(int, input().split()))
l_ls.sort()
stick_count = [0] * (10**3+1)
stick_csum = [0] * (10**3+1)
for i in range(n):
    stick_count[l_ls[i]] += 1
now = 0
for i in range(10**3+1):
    now += stick_count[i]
    stick_csum[i] = now

ans = 0
for first_i in range(n):
    for second_i in range(first_i+1, n):
        #境界は含まない
        greater_than = abs(l_ls[first_i] - l_ls[second_i])
        smaller_than = min(10**3+1,l_ls[first_i] + l_ls[second_i])
        num_canmake = max(0, stick_csum[smaller_than-1] - stick_csum[greater_than])
        if greater_than < l_ls[first_i] < smaller_than:
            num_canmake -= 1
        if greater_than < l_ls[second_i] < smaller_than:
            num_canmake -= 1
        num_canmake = max(0,num_canmake)
        ans += num_canmake
print(ans//3)


