import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    S = readline().strip()
    T = readline().strip()

    idx_in_S = []
    last_idx = 0
    for t in T:
        t_idx = S.find(t, last_idx) + 1
        if t_idx:
            idx_in_S.append(t_idx)
            last_idx = t_idx
        else:
            t_idx = S.find(t, 0, last_idx) + 1
            if not t_idx:
                print(-1)
                exit()
            else:
                idx_in_S.append(t_idx)
                last_idx = t_idx

    
    rep = 0
    for i in range(len(T) - 1):
        if idx_in_S[i] < idx_in_S[i+1]:
            continue
        else:
            rep += 1

    ans = len(S) * rep + idx_in_S[-1]
    print(ans)


if __name__ == "__main__":
    main()
