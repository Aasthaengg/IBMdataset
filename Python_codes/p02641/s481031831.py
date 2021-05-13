# coding: utf-8
# Your code here!
def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
        return 0
    p_list = list(map(int, input().split()))
    
    
    ans = X
    i = 0
    while True:
        tmp_n = X - i
        if tmp_n not in p_list:
            ans = tmp_n
            break
        tmp_p = X + i
        if tmp_p not in p_list:
            ans = tmp_p
            break
        i += 1        
    
    print(ans)

main()