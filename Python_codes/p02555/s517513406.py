S = int(input())

Q = 10 ** 9 + 7
if S < 3:
    print(0)
    exit()

d_list = [-1] * 2001
d_list[3] = 1
d_list[4] = 1
d_list[5] = 1

def ans(n):
    if d_list[n] > 0:
        return d_list[n]
    
    d_list[n] = 1
    # d_list[n] += (n + 1) // 2 + 1
    for i in range(3, n - 2):
        d_list[n] += ans(i)
        d_list[n] %= Q
    
    return d_list[n]

print(ans(S))
