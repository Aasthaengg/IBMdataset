# coding:utf-8
if __name__=='__main__':
    N,K = map(int, input().split())
    if K == 1:
        print(0)
    else:
        print(N-K)