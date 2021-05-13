
def solve():
    j = 1
    for i in s:
        if i != 1:
            print(i)
            exit()
        if j==K:
            print(i)
            exit()
        j += 1
    print(1)

if __name__=="__main__":
    S = input()
    K = int(input())
#    d = 5*10**15
    s = [int(c) for c in S]
#    print(s)
    solve()
