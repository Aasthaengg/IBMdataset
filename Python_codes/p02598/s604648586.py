def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    def isOK(x):
        count = sum((a-1)//x for a in A)
        if count <= K:
            return True
        else:
            return False

    def binary_search(init_l, init_r):
        """(l, r]"""
        left = init_l
        right = init_r

        while right-left > 1:
            mid = (right+left)//2
            if isOK(mid):
                right = mid
            else:
                left = mid

        return right
    
    sum_A = sum(A)
    max_ans = (sum_A + K)//(K+1)
    min_ans = (sum_A + K+N-1)//(K+N)
    ans = binary_search(min_ans-1, max_ans)
    print(ans)
if __name__ == "__main__":
    main()