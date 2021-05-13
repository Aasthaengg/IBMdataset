import math

n, m, x = map(int, input().split())
books = []
for i in range(n):
    books.append(list(map(int, input().split())))
n_bin = '1'*n
_n = (int(n_bin, 2))+1
ans = 10**9

for i in range(_n):
    target = bin(i).replace('0b', '').zfill(n)
    tmp_skill = [0 for i in range(len(books[0])-1)]
    tmp_price = 0
    
    for j in range(len(target)):
        if target[j] == '1':
            tmp_price += books[j][0]
            for k in range(len(tmp_skill)):
                tmp_skill[k] += books[j][k+1]
        for k in range(len(tmp_skill)):
            if tmp_skill[k] < x:
                break
        else:
            ans = min(ans, tmp_price)
if ans == 10**9:
    print(-1)
else:
    print(ans)