n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]

if n == m:
    for i in range(n):
        if a[i] != b[i]:
            break
    else:
        print("Yes")
        exit()
    print("No")
    exit()

for i in range(n-m):
    start_h = i
    end_h = i+m
    for j in range(n-m):
        start_w = j
        end_w = j+m
        for k in range(m):
            if a[start_h+k][start_w:end_w] != b[k]:
                break
        else:
            print("Yes")
            exit()
print("No")

