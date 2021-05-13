N = int(input())
b = list(int(x) for x in input().split())

result = []
while b:
    remove_flag = False
    for i in range(len(b)-1, -1, -1):
        if b[i] == i+1:
            result.insert(0, b.pop(i))
            remove_flag = True
            break
    if not remove_flag:
        print(-1)
        exit()

        remove_flag = False

for i in result:
    print(i)
