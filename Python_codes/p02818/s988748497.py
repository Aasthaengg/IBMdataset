import copy
def main():
    A, B, K = map(int, input().split())
    alterK = copy.copy(K)
    K = K - A
    if K > 0:
        B = B - K
        if B <= 0:
            print('0 0')
            return
        else:
            print('0 ' + str(B))
            return
    else:
        print(str(A - alterK) + ' ' + str(B))
        return
main()