n = int(input())
s = [int(input()) for _ in range(n)]
s.sort()
result = 0
for i in s:
    if i % 10 != 0:
        result = 1
        break

if result == 0:
    print('0')
    exit()

total = sum(s)
if total % 10 == 0:
    for i in range(n):
        total -= s[i]
        if total % 10 == 0:
            total = sum(s)
        else:
            break
print(total)
        
