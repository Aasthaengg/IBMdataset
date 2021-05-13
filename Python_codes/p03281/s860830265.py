import math
def cnt_div(n):
    div = []
    for i in range(1,int(math.sqrt(n)+2)):
        if n%i == 0:
            div.append(i)
            div.append(n//i)
    if len(set(div)) == 8:
        return 1
    else:
        return 0
n = int(input())
ans = 0
for i in range(1,n+1,2):
    ans += cnt_div(i)
print(ans)