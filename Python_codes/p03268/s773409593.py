# -*- coding: utf-8 -*-
"""
@author: H_Hoshigi
"""
def main():
    N, K = map(int, input().split())
    answer = 0
    # m=(N以下の正整数であり、かつKの倍数であるものの個数)とする。
    m = N//K
    # aとbとcが全てKの倍数のとき
    # a,b,cがすべて同じ、うち2つが同じ、3つが相異なるときの場合の数。
    answer += m + m*(m-1)*3 + m*(m-1)*(m-2)

    # Kが偶数のときは、aとbとcが全てKを法として(K//2)に合同なときも条件を満たす。
    if K%2 == 0:
        # m=(N以下の正整数であり、かつKを法として(K//2)に合同なものの個数)とする。
        if m*K + K//2 <= N:
            m += 1
        answer += m + m*(m-1)*3 + m*(m-1)*(m-2)
    print(answer)

if __name__ == "__main__":
    main()

