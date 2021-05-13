import sys


# \n
def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())

    i = 1
    r = 6
    k = 9
    G = [1]
    while r <= N+1:
        G.append(k)
        G.append(r)
        k *= 9
        r *= 6

    number =[10**9] *(N+1)
    number[0]=0

    for i in range(N):
        c = number[i]
        for g in G:
            if i+g <=N:
                number[i+g] =min(c+1,number[i+g])
    print(number[N])



if __name__ == "__main__":
    main()
