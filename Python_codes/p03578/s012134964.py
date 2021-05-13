import collections

def main():
    N = int(input())
    D = [int(_) for _ in input().split()]
    M = int(input())
    T = [int(_) for _ in input().split()]
    Dd = collections.Counter(D)
 
    if N < M:
        print("NO")
        return

    for i in range(M):
        target = T[i]
        if Dd[target] >= 1:
            Dd[target] = Dd[target] - 1
        else:
            print("NO")
            return
    
    print("YES")


if __name__ == "__main__":
    main()