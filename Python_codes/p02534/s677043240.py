def A():
    K = int(input())
    print('ACL'*K)
def B():
    A,B,C,D = map(int,input().split())
    left = max(A,C)
    right = min(B,D)
    if(left <= right):
        print('Yes')
    else:
        print('No')
A()