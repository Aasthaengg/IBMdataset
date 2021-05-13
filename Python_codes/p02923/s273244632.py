N = int(input())
H = list(map(int, input().split()))
K = ["X" if h >= H[i+1] else " " for i, h in enumerate(H[:-1])]
try:
    print(max([len(x) for x in "".join(K).split()]))
except ValueError:
    print(0)
