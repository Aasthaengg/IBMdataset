n=int(input())
cnt=0
for x in range(n):
    for y in range(n):
        if x*4+y*7==n:
            print('Yes')
            exit()
print('No')