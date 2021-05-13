n = int(input())
b = list(map(int, input().split()))

ans = []


while b:
    for i in range(len(b)-1, -1, -1):
        if b[i] == i+1:
            ans.append(i+1)
            del b[i]
            break
    else:
        print(-1)
        exit()
print(*ans[::-1], sep='\n')
