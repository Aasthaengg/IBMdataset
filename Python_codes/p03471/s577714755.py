# coding: utf-8
# Your code here!


n, y= map(int, input().split())
y /= 1000
y = int(y)

ans_i = -1
ans_j = -1
ans_k = -1

for i in range(n+1):
    if ans_i != -1:
        break
    for j in range(n+1-i):
        if n-i-j>=0 and i + j*5 + (n-i-j)*10 == y:
            ans_i = i
            ans_j = j
            ans_k = n-i-j
            break

print(ans_k, ans_j, ans_i)









