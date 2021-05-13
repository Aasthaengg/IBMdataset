def main():

    H, W = map(int, input().split())
    A = []
    for _ in range(H): A.append(input())

    ans = 0
    visited = set()
    for i in range(H):
        for j in range(W):
            if (i, j) not in visited:
                visited.add((i, j))
                b, w = 0, 0
                if A[i][j] == "#":
                    b += 1
                    c = "."
                else:
                    w += 1
                    c = "#"
                cur = [[i, j]]
                while cur:
                    temp = []
                    for k1, l1 in cur:
                        for dk, dl in [[1,0],[-1,0],[0,1],[0,-1]]:
                            k, l = k1+dk, l1+dl
                            if 0<=k<H and 0<=l<W and (k,l) not in visited and A[k][l] == c:
                                visited.add((k,l))
                                temp.append([k, l])

                    if c == "#":
                        b += len(temp)
                        c = "."
                    else:
                        w += len(temp)
                        c = "#"
                    cur = temp
                ans += b*w
    return ans

if __name__ == '__main__':
    print(main())