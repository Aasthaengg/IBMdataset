# string
# a, b, c = input().split()
# str_list = list(input().split())

# number
# a, b, c = map(int, input().split())
# num_list = list(map(int, input().split()))

# lows
# str_list = [input() for _ in range(n)]

# many inputs
# num_list = []
# for i in range(n): num_list.append(list(map(int, input().split())))

n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))

for i in range(n):
    p[i] -= 1

ans = int(-1e14)
for i in range(n):
    tmp = []
    cycle = 0
    index = i
    while True:
        index = p[index]
        tmp.append(c[index])
        cycle += c[index]
        if i == index:
            break
    
    l = len(tmp)
    t = 0
    for j in range(l):
        t += tmp[j]
        if j >= k:
            break
        cur = t
        if cycle > 0:
            e = int((k-j-1) / l)
            cur += e * cycle
        ans = max(cur, ans)
        
print(ans)

