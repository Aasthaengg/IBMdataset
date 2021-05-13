L,R = map(int,input().split())
 
cnt = 0
i = L
j = L+1
min_num = 2020
while i <= R and cnt <= 2019:
    j = i+1
    while j <= R:
        min_num = min(min_num,(i*j)%2019)
        if not min_num:
            break
        j += 1
    i += 1
    cnt += 1
print(min_num)