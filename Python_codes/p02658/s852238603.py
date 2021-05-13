n = int(input())
aa = list(map(int, input().split()))

if 0 in aa:
    print('0')
    exit(0)

result = 1
for a in aa:
    result *= a
    if result > pow(10, 18):
        print('-1')
        exit(0)

print(result)
