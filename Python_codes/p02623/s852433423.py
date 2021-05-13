
if __name__=="__main__":
    N,M,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A_sum_arr,B_sum_arr = [0],[0]
    for i in range(len(A)):
        A_sum_arr.append(A[i]+A_sum_arr[i])
    for i in range(len(B)):
        B_sum_arr.append(B[i]+B_sum_arr[i])
    count = 0
    j = len(B_sum_arr) - 1
    for i,A_sum in enumerate(A_sum_arr):
        if A_sum > K:
            break
        else:
            b_val = K - A_sum
            while b_val < B_sum_arr[j]:
                j -= 1
            count = max(count,(i+j))
    print(count)