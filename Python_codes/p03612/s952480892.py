def main():
    N = int(input())
    P = [int(a) for a in input().split()]

    ans = 0
    for i in range(len(P)):
        if i == len(P) - 1:
            if P[i] == i + 1:
                P[i], P[i - 1] = P[i - 1], P[i]
                ans += 1
            else:
                pass

        else:
            if P[i] == i + 1:
                P[i], P[i + 1] = P[i + 1], P[i]
                ans += 1
            else:
                pass

    print(ans)
    
if __name__ == "__main__":
    main()