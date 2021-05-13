def main():

    N, A, B = map(int, input().split())
    H = []
    for _ in range(N):
        H.append(int(input()))

    l, r = 0, max(H) // B + 1
    while l < r:
        m = (l + r) // 2
        if isvalid(m, H, N, A, B):
            r = m
        else:
            l = m + 1

    return r

def isvalid(n, H, N, A, B):
    alive = []
    for i in range(len(H)):
        if H[i] - n*B > 0:
            alive.append(H[i]-n*B)
    count = 0
    for v in alive:
        if v % (A-B) == 0:
            count += v //(A-B)
        else:
            count += v //(A-B) + 1
    if count <= n:
        return True
    else:
        return False



if __name__ == '__main__':
    print(main())