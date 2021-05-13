N = int(input())
V = list(map(int, input().split()))

dic_odd = {}
dic_even = {}

for i, v in enumerate(V):
    if i % 2 == 0:
        if v in dic_even:
            dic_even[v] += 1
        else:
            dic_even[v] = 1
    else:
        if v in dic_odd:
            dic_odd[v] += 1
        else:
            dic_odd[v] = 1


odd_lst = [(k, v) for k, v in dic_odd.items()]
even_lst = [(k, v) for k, v in dic_even.items()]
odd_lst.sort(key=lambda x: x[1], reverse=True)
even_lst.sort(key=lambda x: x[1], reverse=True)

if (len(odd_lst) == len(even_lst) == 1) and (odd_lst[0][0] == even_lst[0][0]):
    print(int(N / 2))
    exit()

max_ = 0
for a, b in odd_lst:
    for x, y in even_lst:
        if a == x:
            continue
        else:
            max_ = max(b + y, max_)
            break


print(N - max_)
