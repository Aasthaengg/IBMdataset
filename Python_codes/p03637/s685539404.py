from copy import deepcopy

def main():
    n = int(input())
    a = list(map(int, input().split()))
    div2 = [0] * n
    div4 = deepcopy(div2)
    notdiv4 = deepcopy(div2)
    for i in range(n):
        if a[i] % 4 == 0:
            div4[i] = 1
        elif a[i] % 2 == 0:
            div2[i] = 1
        else:
            notdiv4[i] = 1
    num_notdiv4 = sum(notdiv4)
    num_notdiv4 += sum(div2) % 2
    if num_notdiv4 - 1 > sum(div4):
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()
