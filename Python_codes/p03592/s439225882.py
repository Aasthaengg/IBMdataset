# coding: utf-8
(n,m,k) = map(int, input().rstrip().split(" "))

for i in range(n + 1):
    for j in range(m + 1):
        cnt = i*m
        cnt += j*n
        cnt -= i*j*2
        if cnt == k:
            print("Yes")
            exit(0)

print("No")
