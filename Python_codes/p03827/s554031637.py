n = int(input())
S = input()
ans = 0
cur = 0
for i in S:
    if i == 'I':
        cur += 1
    else:
        cur -= 1
    ans = max(ans, cur)
    
print(ans)