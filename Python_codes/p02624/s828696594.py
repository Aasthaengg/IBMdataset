if __name__ == "__main__":
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        val = i
        d = n//i
        val *= d*(d+1)//2
        ans += val
        #print(i, d, val)
    print(ans)
