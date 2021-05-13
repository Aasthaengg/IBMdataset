def main():
    N = int(input())
    sheet = 0
    for i in range(N):
        l, r = map(int, input().split())
        sheet += (r-l) + 1
    print(sheet)
main()