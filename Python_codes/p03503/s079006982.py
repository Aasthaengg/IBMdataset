def solve(n, f_list, p_list):

    ans = [0] * 1024
    
    for i in range(1, 1024):
        for f, p in zip(f_list, p_list):
            c = bin(f & i).count("1")
            ans[i] += p[c]
    
    return max(ans[1:])

if __name__ == "__main__":
    n = int(input())
    f_list = [int("".join(input().split()),2) for i in range(n)]
    p_list = [[int(j) for j in input().split()] for i in range(n)]
    print(solve(n, f_list, p_list))