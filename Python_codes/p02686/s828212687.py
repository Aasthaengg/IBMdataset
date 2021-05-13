def main():
    import queue
    import sys
    input = lambda : sys.stdin.readline().rstrip()
    sys.setrecursionlimit(max(1000, 10**9))



    n = int(input())
    minsum = [None] * n # (min, sum)
    for i in range(n):
        tmp = list(map(int, " ".join(input()).replace("(", "1").replace(")", "-1").split()))
        c = 0
        m = 0
        for item in tmp:
            c += item
            m = min(c, m)
        minsum[i] = (m, sum(tmp))
    minsum.sort()

    if sum(item[1] for item in minsum)!=0:
        print("No")
    else:
        minsum1 = [item for item in minsum if item[1]>=0]
        minsum2 = [(item[0]-item[1], -item[1]) for item in minsum if item[1]<0]
        minsum2.sort()
        c = 0
        for m,s in minsum1[::-1]:
            if c+m>=0:
                c += s
            else:
                print("No")
                return
        c = 0
        for m,s in minsum2[::-1]:
            if c+m>=0:
                c+=s
            else:
                print("No")
                return
        print("Yes")
main()