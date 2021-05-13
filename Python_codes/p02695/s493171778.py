from itertools import combinations_with_replacement

n, m, q = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(q)]

temp = list(combinations_with_replacement([i for i in range(1,m+1)],n))

ans = 0

for a_temp in temp:
    ans_temp = 0
    for i in range(q):
        if a_temp[a[i][1]-1] - a_temp[a[i][0]-1] == a[i][2]:
            ans_temp += a[i][3]
    if ans < ans_temp:
        ans = ans_temp
        
print(ans)