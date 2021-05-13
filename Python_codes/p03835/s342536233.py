
def resolve():
    ks = input().split(" ")
    k = int(ks[0])
    s = int(ks[1])

    n = 0

    for zz in range(k+1):
        for yy in range (k+1):
                if (0 <= s-(yy+zz) <= k):
                    n += 1

    print(n)

if __name__ == "__main__":
    resolve()