def two_int():
    N, K = map(int, input().split())
    return N,K

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))

H,W,A,B = map(int, input().split())

for h in range(H):
    if h>=B:
        temp = "1"*A
        temp += "0"*(W-A)
    else:
        temp = "0"*A
        temp += "1"*(W-A)
    print(temp)