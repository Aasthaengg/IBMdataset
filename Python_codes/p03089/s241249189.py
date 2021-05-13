N = int(input())
b = list(map(int, input().split()))

ans = []

while b:
    for i in reversed(range(len(b))):
        if b[i] == i+1:
            del(b[i])
            ans.append(i+1)
            break
    else:
        if b:
            print(-1)
            exit()

for a in reversed(ans):
    print(a)