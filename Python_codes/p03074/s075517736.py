n,k = map(int,input().split())

s=list(input())

border = [0]

for i in range(1,n):
    if s[i-1] != s[i]:
        border.append(i)

border_count = len(border)

ans = 0

for i in range(border_count):
    if s[border[i]] == '0':
        block_1 = i+k*2
    else:
        block_1 = i+k*2+1
    #print(block_1, border)
    if block_1 < border_count:
        ans = max(ans, border[block_1]-border[i])
    else:
        ans = max(ans, n-border[i])
print(ans)
