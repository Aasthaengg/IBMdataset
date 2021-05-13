N = int(input())
S = [int(input()) for _ in range(N)]
total = sum(S)
if total % 10 != 0:
    print(total)
else:
    ans = list(filter(lambda x: x % 10 != 0, S))
    if len(ans):
        print(total - min(ans))
    else:
        print(0)
