from collections import Counter

if __name__ == '__main__':

    n = int(input())
    A = list(map(int,input().split()))

    #全体の数
    d = Counter(A)
    
    d2 = dict()
    #この時の組み合わせの合計
    for k,v in d.items():
        d2[k] = (v*(v-1)) // 2
    ans_sum = sum(d2.values())

    #結果表示
    for i in A:
        ans = 0
        if i in d2:
            #あるならば
            tmp = d[i] - 1
            before= d2[i]
            after = (tmp*(tmp-1)) //2
            ans = ans_sum - (before-after)
            print(ans)
        else:
            #ないならば
            print(ans_sum)
