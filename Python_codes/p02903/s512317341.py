def main():

    H, W, A, B = map(int, input().split())
    isfound = False
    for m in range(H+1):
        for n in range(W+1):
            if m*A + (H-m)*(W-A) == n*B + (W-n)*(H-B):
                isfound = True
                p, q = m, n
                break
        if isfound:
            break
    if not isfound:
        return "No"

    count = [B for _ in range(q)] + [H-B for _ in range(W-q)]

    for i in range(p):
        temp = []
        cnt = A
        for j in range(W):
            if count[j] > 0 and cnt > 0:
                cnt -= 1
                count[j] -= 1
                temp.append(1)
            else:
                temp.append(0)
        print("".join(map(str, temp)))

    for i in range(H-p):
        temp = []
        cnt = W-A
        for j in range(W):
            if count[j] > 0 and cnt > 0:
                cnt -= 1
                count[j] -= 1
                temp.append(1)
            else:
                temp.append(0)
        print("".join(map(str, temp)))


if __name__ == '__main__':
    main()