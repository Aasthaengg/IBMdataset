import math

def cut(l,A,K):
    counter = 0
    i = N - 1
    if l == 0:
        return False
    while i >= 0:
        c = math.ceil(A[i] / l) - 1
        if c == 0:
            break
        else:
            counter += c
            i -= 1
    if counter <= K:
        return True
    else:
        return False
    
if __name__ == '__main__':
    N,K = map(int,input().split())
    A = [float(a) for a in input().split()]
    A.sort()
    left = 0
    right = math.ceil(A[-1])
    while left <= right:
        middle = (left + right) // 2
        if cut(middle,A,K):
            if not cut(middle-1,A,K):
                break
            else:
                right = middle - 1
        else:
            left = middle + 1
    print(middle)