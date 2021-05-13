n = int(input())
cnt = 0
for i in map(int,input().split()):
    if i % 2 == 0:
        cnt += 1
print(3**n-2**cnt)