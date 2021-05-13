
def solve():
    l = len(S)
    R  = [-1]*26
    R1 = [-1]*26
    is_ok = True
    for i in range(l):
        S_num = ord(S[i]) - ord("a")
        T_num = ord(T[i]) - ord("a")
        if R[S_num] == -1:
            R[S_num] = T_num
        else:
            if R[S_num] != T_num:
                is_ok = False
                break
        if R1[T_num] == -1:
            R1[T_num] = S_num
        else:
            if R1[T_num] != S_num:
                is_ok = False
                break
        
    if is_ok:
        print("Yes")
    else:
        print("No")


if __name__=="__main__":
    S = input()
    T = input()
#    S = [c for c in s]
#    T = [c for c in t]
    solve()
