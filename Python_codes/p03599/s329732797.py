from sys import stdin


if __name__ == "__main__":
    _in = [_.rstrip() for _ in stdin.readlines()]
    A,B,C,D,E,F = list(map(int,_in[0].split(' ')))  # type:list(int)
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    per = -1
    for a in range(0,F+1,100*A):
        for b in range(0,F+1,100*B):
            if a+b == 0:
                break
            for c in range(0,F+1,C):
                for d in range(0,F+1,D):
                    if a+b+c+d>F:
                        break
                    elif (c+d)/(a+b)>E/100:
                        break
                    else:
                        if per < (c+d)/(a+b+c+d):
                            per = (c+d)/(a+b+c+d)
                            cnt = [a+b+c+d, c+d]
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(cnt[0],cnt[1])
