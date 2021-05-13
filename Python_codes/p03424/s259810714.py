n = int(input())
s = list(input().split())
for x in s:
    if x == 'Y':
        print('Four')
        exit()
print('Three')