def resolve():
    N = int(input())
    L = list(map(int, input().split(" ")))
    maxL = max(L)
    totalL = sum(L)
    print("Yes" if maxL < totalL - maxL else "No")
    

if '__main__' == __name__:
    resolve()