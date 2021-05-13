
def solve():
    k = 0
    N = n
    ans = ""
    if n == 0:
        print(0)
        exit()
    while N:
        k+=1
        if N % 2 == 1:
#            print("------\t" + str(N))
            N -= 1
            ans += "1"
        else:
            ans += "0"
        N //= (-2)  # n=-2 進数
#        print(N)
#    print(k)    #   桁数
    print(ans[::-1])
#    print(a[::-1])



if __name__=="__main__":
    n = int(input())
    solve()

