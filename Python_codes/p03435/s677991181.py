li = [list(map(int,input().split())) for i in range(3)]
ans = li[0]

for i in li:
    for j in range(-100,102):
        if j == 101:
            print("No")
            exit()
        if [i+j for i in ans] == i:
            break

print("Yes")