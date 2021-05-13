def main():
    S = list(input())
    tmp = list('keyence')
    st = -1; ed = -1
    if S[0] == tmp[0]:
        st = 0
        for i in range(1, len(tmp)):
            if S[i] == tmp[i]:
                st += 1
            else:
                break
    if st+1 == len(tmp):
        print('YES')
        return
    if S[-1] == tmp[-1]:
        ed = 0
        for i in range(1, len(tmp)):
            if S[-1-i] == tmp[-1-i]:
                ed += 1
            else:
                break
    if ed+1 == len(tmp):
        print('YES')
        return
    if st == -1 or ed == -1:
        print('NO')
        return
    rm = (st+1 + ed+1) - len(tmp)
    if rm >= 0:
        s = tmp[:st+1] + tmp[-ed-1+rm:]
        if s == tmp:
            print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()
