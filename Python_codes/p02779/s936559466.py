def main():
    """"ここに今までのコード"""
    N = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort()
    distinctFlg = False

    for i in range(N - 1):
        if num_list[i] == num_list[i+1]:
            distinctFlg = True
            break
    
    if distinctFlg:
        print("NO")
    else:
        print("YES")

if __name__ == '__main__':
    main()