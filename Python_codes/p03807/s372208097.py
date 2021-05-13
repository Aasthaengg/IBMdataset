
if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    odd = 0
    even = 0
    for a in A:
        if a % 2:
            odd+=1
        else:
            even+=1
    if odd % 2 == 1:
        print('NO')
    else:
        print('YES')


