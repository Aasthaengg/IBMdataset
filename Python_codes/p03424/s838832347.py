n = int(input())
s = list(input().split())
cnt = 0

for i in range(n):
    if s[i] == 'Y':
        cnt += 1

if cnt == 0:
    print('Three')
else:
    print('Four')