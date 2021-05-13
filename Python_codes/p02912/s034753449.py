n, m = map(int, input().split())
A = list(map(int, input().split()))

tmp_list = []

for i in range(n):
    tmp = A[i]
    now = tmp
    while True:
        if tmp != 0:
            tmp = tmp // (2)
            tmp_list.append(now - tmp)
            now = tmp
        else:
            break

tmp_list.sort(reverse=True)
print(sum(A) - sum(tmp_list[:m])) 