n = int(input())
a_li = list(map(int, input().split()))
b_li = list(map(int, input().split()))

if sum(a_li) < sum(b_li):
    print(-1)
    exit()
    
check = [0]*n
cnt = 0
SUM_ma = 0

for i in range(n):
    check[i] = a_li[i] - b_li[i]
    
    if check[i] < 0:
        cnt += 1
        SUM_ma += check[i]

if SUM_ma < 0:
        
    check.sort(reverse=True)
    
    for i in check:
        SUM_ma += i
        cnt += 1
        
        if SUM_ma >= 0:
            break
        
print(cnt)