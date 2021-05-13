def main():
    n = int(input())
    s = list(input())

    s_b = [1 if c=='#' else 0 for c in s]
    s_w = [1 if c=='.' else 0 for c in s[::-1]]

    s_b = cumsum(s_b)
    s_w = cumsum(s_w)[::-1]

    ans = []
    for i in range(n):
        ans.append(s_b[i]+s_w[i+1])

    print(min(ans))

def cumsum(a):
    s = 0
    sums = [0]
    for a_i in a:
        s+=a_i
        sums.append(s)

    return sums


if __name__ == "__main__":
    main()