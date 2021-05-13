import sys
n = int(input())
a_ls = [int(i) for i in sys.stdin.readline().split()]
start = 0
end = 1
a_ls = [bin(i)[2:].zfill(20) for i in a_ls] + ["2" * 20]
dic = {i : 0 if j == "0" else 1 for i,j in enumerate(a_ls[0])}
cnt = 0
while start < n and end <= n:
    flg = True
    a = a_ls[end]
    for i, j in enumerate(a):
        if dic[i] + int(j) > 1:
            flg = False
    if flg:
        for i, j in enumerate(a):
            dic[i] += int(j)
        end += 1
    else:
        cnt += (end - start - 1)
        for i, j in enumerate(a_ls[start]):
            dic[i] -= int(j)
        start += 1
        if end == start:
            for i, j in enumerate(a):
                dic[i] += int(j)
            end += 1
print(cnt + n)