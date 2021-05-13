# これかなり難しくないですか
# 解説見た...

n = int(input())
b_lis = list(map(int, input().split()))
ans = []
while b_lis:
    tmp = -1
    for i, v in enumerate(b_lis):
        if v == i + 1:
            tmp = i
    if tmp >= 0:
        ans.append(tmp + 1)
        b_lis = b_lis[:tmp] + b_lis[tmp + 1 :]
    else:
        print(tmp)
        exit()

for v in ans[::-1]:
    print(v)

