from sys import stdin

def readString() :
    return  stdin.readline().rstrip()

def solve() :
    S = "CODEFESTIVAL2016"
    T = stdin.readline().rstrip()
    ans = 0 
    for x in range(len(S)):
        if(S[x] != T[x]) :
            ans += 1

    print(ans)

solve()