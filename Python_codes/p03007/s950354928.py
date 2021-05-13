def main():
    n = int(input())
    a = list(map(int, input().split()))
    neg = []
    pos = []
    for v in a:
        if v < 0:
            neg.append(v)
        else:
            pos.append(v)
    ans = []
    neg.sort()
    x, y = 0, len(neg)-1
    if len(pos) == 0:
        ans.append([neg[y], neg[x]])
        p = neg[y] - neg[x]
        pos.append(p)
        x += 1
        y -= 1
    for i in range(x, y):
        ans.append([pos[0], neg[i]])
        pos[0] -= neg[i]
    if y-x+1 > 0:
        pos.append(neg[y])
    pos.sort()
    for i in range(len(pos)-2):
        ans.append([pos[i], pos[i+1]])
        pos[i+1] = pos[i] - pos[i+1]
    if len(pos) > 1:
        ans.append([pos[len(pos)-1], pos[len(pos)-2]])
        pos[len(pos)-1] = pos[len(pos)-1] - pos[len(pos)-2]
    print(pos[len(pos)-1])
    for p, q in ans:
        print(p, q)

if __name__ == "__main__":
    main()
