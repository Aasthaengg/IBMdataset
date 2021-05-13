n = int(input())
sp = [0] * n
for i in range(n):
    sp[i] = list(map(str,input().split()))
sp_sorted = sorted(sp, key=lambda x: int(x[1]), reverse=True)
sp_sorted_sorted = sorted(sp_sorted, key=lambda x: x[0])
for i in range(n):
    for j in range(n):
        if sp_sorted_sorted[i] == sp[j]:
            print(j+1)