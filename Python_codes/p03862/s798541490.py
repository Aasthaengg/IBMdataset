def solve(n, x, a_list):
    
    ans = 0
    for i in range(len(a_list)-1):
        tmp = a_list[i] + a_list[i+1]
        if tmp > x:
            d = tmp - x
            ans += d
            if a_list[i+1] - d >= 0:
                a_list[i+1] = a_list[i+1] -d
            else:
                a_list[i] = a_list[i] - (d-a_list[i+1])
                a_list[i+1] = 0
    return ans

if __name__ == "__main__":
    n, x = [int(i) for i in input().split()]
    a_list = [int(i) for i in input().split()]
    print(solve(n, x, a_list))