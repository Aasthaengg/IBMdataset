n, k = map(int, input().split())
s = list(input())

# 連続で0か1が連なっているリストを作成
# (0or1, 個数)
sum_s = []
cnt = 0
flag = int(s[0])
if flag == 0:
    sum_s.append((1, 0))
flag = int(s[0])
for i in range(n):
    if s[i] == '0':
        if flag == 0:
            cnt += 1
        else:
            sum_s.append((flag, cnt))
            flag, cnt = 0, 1
    else:
        if flag == 0:
            sum_s.append((flag, cnt))
            flag, cnt = 1, 1
        else:
            cnt += 1
sum_s.append((flag, cnt))
#print(sum_s)

# 累積和
rs = [0] * (len(sum_s)+1)
for i in range(1, len(sum_s)+1):
    rs[i] = rs[i-1] + sum_s[i-1][1]

ans = 0

#print(rs)
length = 2*k+1
for i in range(0, len(sum_s)+1, 2):
    ans = max(ans, rs[min(i+length, len(sum_s))] - rs[i])
    #print(ans, min(i+length, len(sum_s)), i)
print(ans)