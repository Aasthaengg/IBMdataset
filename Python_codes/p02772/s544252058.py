n = int(input())
a = map(int, input().split())

ans = 'APPROVED'
for a_i in a:
    if a_i % 2 == 0:
        if not ((a_i % 3 == 0) or (a_i % 5 == 0)):
            ans = 'DENIED' 
            break
print(ans)
