N,M = map(int, input().split())
Ai = [int(i) for i in input().split()]

remain = N - sum(Ai)
if remain < 0:
    print("-1")
else:
    print(f"{remain}")