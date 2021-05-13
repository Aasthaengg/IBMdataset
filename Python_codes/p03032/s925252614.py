from itertools import accumulate
n, k = map(int, input().split())
vs = list(map(int, input().split()))
res = 0
for i in range(min(n,k)+1):
    for j in range(min(n-i,k-i)+1):
        res_tmp = 0
        arr = []
        if i > 0:
            arr += vs[:i]
        if j > 0:
            arr += vs[(n-j):]
        if arr != []:
            arr.sort()
            n_len = len(arr)
            for m in range(min(k-i-j,n_len)):
                if arr[m] >= 0:
                    break
                res_tmp -= arr[m]
            res_tmp += sum(arr)
        res = max(res,res_tmp)
print(res)