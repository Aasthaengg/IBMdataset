N = int(input())
b = list(map(int,input().split()))
l = []
while b:
    for i in range(len(b)-1,-1,-1):
        if b[i] == i + 1:
            del b[i]
            l += i + 1,
            break
    else:
        print(-1)
        exit()
for i in l[::-1]:
    print(i)