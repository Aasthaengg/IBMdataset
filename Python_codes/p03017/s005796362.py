N, A, B, C, D = map(int, input().split())
S = str(input())

# ##となっていたら無理
# C < D のとき、それぞれが移動可能かでわかる
# C > D のときは? 追い越しは...となる箇所があればいける

if '##' in S[min(A, B)-1:max(D, C)]:
    print('No')
    quit()

if C < D:
    print('Yes')
else:
    if '...' in S[B-2:D+1]:
        print('Yes')
        quit()
    print('No')