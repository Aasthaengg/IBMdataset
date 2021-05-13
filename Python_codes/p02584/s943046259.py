def main():
    in_list = list(map(int, input().split()))
    X = abs(in_list[0])
    K = in_list[1]
    D = in_list[2]

    max_move = K*D
    if max_move < X:
        print(X-max_move)
    else:
        iter1 = int(X/D)+1
        iter2 = K - iter1
        ans = X - iter1*D
        if iter2%2 == 0:
            print(abs(ans))
        else:
            print(abs(ans+D))

if __name__ == "__main__":
    main()