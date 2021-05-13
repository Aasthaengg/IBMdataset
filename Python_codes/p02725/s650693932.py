# coding: utf-8

def main():
    k, n = map(int, input().split())
    A_array = list(map(int, input().split()))
    A_array.sort()
    # print(A_array, A_array[-1])
    
    
    ans = float("inf")
    for i in range(n):
        if i == 0:
            d_r = A_array[-1] - A_array[0]
            d_l = k - (A_array[1] - A_array[0])
            d = min(d_r, d_l)
        elif i == n - 1:
            d_r = k - (A_array[-1] - A_array[-2])
            d_l = A_array[-1] - A_array[0]
            d = min(d_r, d_l)
        else:
            d_r = k - (A_array[i] - A_array[i-1])
            d_l = A_array[i] + (k - A_array[i+1])
            d = min(d_l, d_r)
        # print(d)
        ans = min(ans, d)
    print(ans)
main()