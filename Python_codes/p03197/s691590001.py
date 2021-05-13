def main():
    #残っている色の個数が偶数になるように行動
    N = int(input())
    A = list()
    for _ in range(N):
        if int(input()) % 2 == 1:
            break
    else:
        print('second')
        return
    print('first')
    return
    

    
main()