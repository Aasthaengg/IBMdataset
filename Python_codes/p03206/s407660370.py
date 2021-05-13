def resolve():
    D = int(input())
    ans = "Christmas"
    for i in range(25-D):
        ans += " Eve"
    print(ans)

if '__main__' == __name__:
    resolve()