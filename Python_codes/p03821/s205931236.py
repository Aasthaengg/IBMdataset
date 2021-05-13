n = int(input())
a_li = []
b_li = []
for _ in range(n):
    a,b = map(int, input().split())
    a_li.append(a)
    b_li.append(b)

cnt = 0
for i in range(1,n+1):
    if (a_li[-i]+cnt) % b_li[-i] != 0:
        cnt += b_li[-i] - ((a_li[-i]+cnt) % b_li[-i])
print(cnt)
