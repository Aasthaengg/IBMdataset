n = int(input())
d_list = list(map(int, input().split()))
m = int(input())
t_list = list(map(int, input().split()))

sorted_d = sorted(d_list)
sorted_t = sorted(t_list)

d_index = 0
d_len = len(sorted_d)
for t in sorted_t:
    found = False
    for i in range(d_index, d_len):
        if t < sorted_d[i]:
            print('NO')
            exit()
        if t == sorted_d[i]:
            d_index = i+1
            found = True
            break
    if not found:
        print('NO')
        exit()

print('YES')

