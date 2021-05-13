if __name__ == '__main__':
    n = int(input())
    A = list(map(int,input().split()))

    ans = 0

    while True:
        
        #全列が0ならば探索終了
        if max(A) == 0:
            break
        
        i = 0
        
        #１列 横に調査
        while i < n:
        
            if A[i] == 0:
                #横にずらす
                i += 1
            else:
                #カウント++
                ans += 1

                #最後か0にぶつかるまで,列の値を１マイナスする
                while i < n and A[i] != 0:
                    #1ずつマイナスする
                    A[i] -= 1
                    #横にずらす
                    i += 1
    print(ans)