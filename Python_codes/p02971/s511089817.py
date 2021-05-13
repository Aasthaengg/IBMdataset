N = int(input())
aaa = [int(input()) for _ in range(N)]
MAX = max(aaa)
NEX = sorted(aaa)[-2]
for a in aaa:
    if a < MAX:
        print(MAX)
    else:
        print(NEX)
