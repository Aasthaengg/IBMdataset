import sys
import bisect

# \n
def input():
    return sys.stdin.readline().rstrip()


def main():
    S = list(input())
    T =list(input())

    G =[[] for _ in range(26)]

    orda =ord("a")

    for i in range(len(S)):
        G[ord(S[i])-orda].append(i)

    count =0
    p=-1
    for j in range(len(T)):
        tord = ord(T[j]) -orda
        if G[tord]!=[]:
            if G[tord][-1]<p+1:
                p=-1
                count+=1

            gp =bisect.bisect_left(G[tord],p+1)
            p =G[tord][gp]

        else:
            print(-1)
            exit()


    print(count * len(S)+p+1)





if __name__ == "__main__":
    main()
