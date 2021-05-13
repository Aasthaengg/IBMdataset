
def solve():
    N = int(input())
    b = list(map(int, input().split()))
    del_list = []

    while True:
        del_index = -1
        for k in range(len(b)):
            if b[k] == k + 1:
                del_index = max(del_index, k)
        if del_index < 0:
            break
        else:
            del_list.append(b[del_index])
            b.pop(del_index)

    if len(b) > 0:
        print(-1)
    else:
        for key in del_list[::-1]:
            print(key)

solve()