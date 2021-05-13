
def main():
    d, n = map(int, input().split())
    dd = 100**d
    if n%100 != 0:
        ans = n*dd
    else:
        ans = (1+n)*dd
    print(ans)
main()