def linearSearch(S, T):
    n = 0
    for t in T:
        for s in S:
            if s == t:
                n += 1
                break
    return n

if __name__ == "__main__":
    input()
    S = raw_input().split()
    input()
    T = raw_input().split()
    print linearSearch(S, T)