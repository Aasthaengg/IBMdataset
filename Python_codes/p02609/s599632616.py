import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    N = int(readline())
    X_bin = readline().strip()
    n = X_bin.count("1")
    X = int(X_bin, 2)

    X_pop_p = X % (n + 1)
    if n != 1:
        X_pop_m = X % (n - 1)

    
    def count(x):
        cnt = 1
        while x:
            x %= bin(x).count("1")
            cnt += 1
        return cnt
        
    ans = []
    for i in range(N):
        X_i = X ^ (1 << i)
        if X_i == 0:
            ans.append(0)
        else:
            if X_bin[-(i+1)] == "1":
                mod = (X_pop_m - pow(2, i, n - 1)) % (n - 1)
                ans.append(count(mod))
            else:
                mod = (X_pop_p + pow(2, i, n + 1)) % (n + 1)
                ans.append(count(mod))

    print("\n".join(map(str, ans[::-1])))


if __name__ == "__main__":
    main()
