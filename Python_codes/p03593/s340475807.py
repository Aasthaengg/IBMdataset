def main():
    h, w = map(int, input().split())
    alp = [0]*26
    for _ in range(h):
        s = input()
        for c in s:
            p = ord(c) - ord("a")
            alp[p] += 1
    f = True
    cnt_1, cnt_2, cnt_4 = 0, 0, 0
    if h%2 == 1 and w%2 == 1:
        cnt_1 = 1
        cnt_2 = w-1 + h-1
        cnt_4 = (w-1)*(h-1)
    elif h%2 == 1 and w%2 == 0:
        cnt_2 = w
        cnt_4 = w*(h-1)
    elif h%2 == 0 and w%2 == 1:
        cnt_2 = h
        cnt_4 = (w-1)*h
    else:
        cnt_4 = w*h
    for i in range(26):
        while cnt_4 > 0 and alp[i]>=4:
            alp[i] -= 4
            cnt_4 -= 4
    if cnt_4 > 0:
        f = False
    for i in range(26):
        while cnt_2 > 0 and alp[i]>=2:
            alp[i] -= 2
            cnt_2 -= 2
    if cnt_2 > 0:
        f = False
    for i in range(26):
        while cnt_1 > 0 and alp[i]>=1:
            alp[i] -= 1
            cnt_1 -= 1
    if cnt_1 > 0:
        f = False
    if f:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
