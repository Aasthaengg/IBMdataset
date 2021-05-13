def main():
    n,k = map(int,input().split())
    v = list(map(int,input().split()))
    m = 0
    for k_ in range(k+1):
        v_c = v
        if k_>n:
            v_ = v_c
            v_c = []
            s = k-n
        else:
            v_ = v_c[0:k_]
            v_c = v_c[k_:]
            s = k-k_
        for i in range(s+1):
            if i>len(v_c):
                v__ =v_+ v_c
                s_ = s-len(v_c)
            else:
                v__ = v_+ v_c[len(v_c)-i:]
                s_ = s-i
            while s_>0 and len(v__)>0 and min(v__)<0:
                v__.pop(v__.index(min(v__)))
                s_ = s_-1
            if sum(v__)>m:
                m = sum(v__)
    print(m)

if __name__ == "__main__":
    main()