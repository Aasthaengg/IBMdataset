import sys


# \n
def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    S = list(input())



    ans =0
    for k in range(N+1,0,-1):
        i=0
        count =0
        while i<N-k:
            if S[i]==S[i+k]:
                count+=1
                ans =max(ans,min(count,k))
            else:
                count=0

            i+=1

    print(ans)









if __name__ == "__main__":
    main()
