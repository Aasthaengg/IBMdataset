n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))
x = {}
for i in d:
    if i in x:
        x[i] += 1
    else:
        x[i] = 1
t.sort()
j, cnt = t[0], 0
for i in t:
    if i == j:
        cnt += 1
    else:
        if not j in x:
            print("NO")
            exit()
        else:
            if cnt > x[j]:
                print("NO")
                exit()
            j, cnt = i, 1
if not j in x:
    print("NO")
    exit()
else:
    if cnt > x[j]:
        print("NO")
        exit()
    j, cnt = i, 1
print("YES")