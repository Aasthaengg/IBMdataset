n = int(input())
d = [[] for _ in range(n)]
for i in range(n):
    d[i] = list(map(int, input().split()))
counter = 0
for i in d:
    if i[0] == i[1]:
        if counter == 2:
            print("Yes")
            exit()
        else:
            counter += 1
    else:
        counter = 0
print("No")