def resolve():
    '''
    code here
    '''
    N = int(input())
    As = [int(input()) for _ in range(N)]

    max_num = max(As)
    max_index = As.index(max_num)

    for i in range(N):
        if i == max_index:
            As.remove(max_num)
            print(max(As))
        else:
            print(max_num)
if __name__ == "__main__":
    resolve()
