from math import ceil

def check(N_:int,S_:list,F_:list,upper:int,K_:int)->bool:
    #A_i > A_j (i < j)
    cnt = 0
    for i in range(N_):
        s = S_[i]
        if s > upper:
            cnt += ceil((s - upper)/F_[i])
            if cnt > K_:
                return False
    return True


def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    F = list(map(int,input().split()))
    A.sort(reverse = True)
    F.sort()
    S = [f*a for f,a in zip(F,A)]
    right = max(S)
    left = -1
    while left + 1 < right:
        mid = (right + left) // 2
        if mid == right:
            break
        if check(N,S,F,mid,K):
            right = mid
        else:
            left = mid
    print(right)
    return

if __name__ == "__main__":
    main()