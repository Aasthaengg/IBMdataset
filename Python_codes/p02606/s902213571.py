def main():

    L, R, d = map(int, input().split())

    num_R = R // d
    num_L = (L-1) // d

    ans = num_R - num_L

    print(ans)

if __name__ == "__main__":
    main()