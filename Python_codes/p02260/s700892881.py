def serect_sort(r, n):
    cnt = 0
    for i in range(0, n):
        minj = i
        for j in range(i, n):
            if r[j] < r[minj]:
                minj = j
        r[i],r[minj] = r[minj],r[i]
        if i != minj:
            cnt +=1
    print(*r)
    print(cnt)

N = int(input())
A = list(map(int, input().split()))
serect_sort(A, N)