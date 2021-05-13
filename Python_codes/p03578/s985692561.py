from collections import defaultdict
def main():
    N = int(input())
    D = [int(d) for d in input().split()]
    M = int(input())
    T = [int(t) for t in input().split()]

    diff = defaultdict(int)

    for i in range(len(D)):
        diff[D[i]] += 1

    ok = True
    for i in range(len(T)):
        if diff[T[i]] >= 1:
            diff[T[i]] -= 1
        else:
            ok = False
            break

    if ok:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()