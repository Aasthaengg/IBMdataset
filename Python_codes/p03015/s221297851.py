import sys
#input = sys.stdin.buffer.readline

def main():
    L = str(input())
    MOD = 10**9+7
    dpa = [1]
    dpb = [2]
    N = len(L)
    for i in range(1,N):
        if L[i] == "1":
            dpa.append((dpa[-1]*3+dpb[-1])%MOD)
            dpb.append((dpb[-1]*2)%MOD)
        else:
            dpa.append((dpa[-1]*3)%MOD)
            dpb.append((dpb[-1])%MOD)
            
    print((dpa[-1]+dpb[-1])%MOD)

if __name__ == "__main__":
    main()