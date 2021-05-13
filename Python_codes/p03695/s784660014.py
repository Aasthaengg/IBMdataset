n = int(input())
#n, k = map(int, input().split())
al = list(map(int, input().split()))
#al=[list(input()) for i in range(n)]


def color(rate):
    c = rate//400
    return min(8, c)


dic = {i: 0 for i in range(9)}

for a in al:
    dic[color(a)] = dic[color(a)]+1

count = 0
for i in range(8):
    if dic[i] != 0:
        count += 1

mn = count
mx = count
if dic[8] != 0:
    if count>=1:
        mx = mn+dic[8]
    else:
        mn=1
        mx=dic[8]

print(mn, mx)
