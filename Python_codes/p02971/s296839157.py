n = int(input())
a = list(int(input()) for _ in range(n))

l = sorted(a)

max_num = l[-1]
sec_max = l[-2]

cnt = a.count(max_num)

for x in a:
    if x == max_num and cnt == 1:
        print(sec_max)
    else:
        print(max_num)
