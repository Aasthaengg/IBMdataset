def main():
    S = input()
    A = [ 0 for i in range(len(S) + 1)]

    idx_list = list([0])
    part = list()

    for i in range(len(S) - 1):
        if S[i] == ">" and S[i+1] == "<":
            idx_list.append(i+1)

    idx_list.append(len(S))

    if len(idx_list) == 1:
        part.append(S)
    else:
        for i in range(len(idx_list) - 1):
            part.append(S[idx_list[i]:idx_list[i+1]])

    ans = 0
    for p in part:
        G, L = 0, 0

        for j in range(len(p)):
            if p[j] == "<":
                G += 1
            else:
                L += 1

        tmp = 0
        if G < L:
            tmp += L*(L+1)//2 + G*(G-1)//2
        elif G > L:
            tmp += G*(G+1)//2 + L*(L-1)//2
        else:
            tmp += G*(G+1)//2 + L*(L-1)//2

        ans += tmp
        
    print(ans)

if __name__ == "__main__":
    main()