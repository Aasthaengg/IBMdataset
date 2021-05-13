n, k = map(int, input().split())
s = str(input())

count = 1
Nums_count = []
now = s[0]
start = 0
for i in range(1,n):
    if s[i] == str(now):
        count += 1
    else:
        Nums_count.append([start, count])
        now = s[i]
        start = i
        count = 1
    if i == n-1:
        Nums_count.append([start, count])
if len(s) == 1:
    Nums_count.append([0,1])

Nums_count_rui = [[-1, 0]]
for i in range(len(Nums_count)):
    Nums_count_rui.append([Nums_count[i][0],Nums_count[i][1]+Nums_count_rui[-1][1]])

# print(Nums_count_rui)
ans = 0
m = len(Nums_count_rui)

if s[0] == '0' and m <= 2*k:
    ans = n
elif s[0] == '1' and m <= 2*k+1:
    ans = n

for i in range(1,m):
    if s[Nums_count_rui[i][0]] == '0':
        if i+2*k-1 >= m:
            tot = Nums_count_rui[-1][1] - Nums_count_rui[i-1][1]
        else:
            tot = Nums_count_rui[i+2*k-1][1] - Nums_count_rui[i-1][1]
    else:
        if i+2*k >= m:
            tot = Nums_count_rui[-1][1] - Nums_count_rui[i-1][1]
        else:
            tot = Nums_count_rui[i+2*k][1] - Nums_count_rui[i-1][1]
    ans = max(tot, ans)
print(ans)