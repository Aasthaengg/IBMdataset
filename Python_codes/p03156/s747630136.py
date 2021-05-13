n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))
easy = []
norm = []
hard = []
for pi in p:
    if pi <= a:
        easy.append(pi)
    elif a < pi <= b:
        norm.append(pi)
    else:
        hard.append(pi)

ans = min(len(easy), len(norm))
ans = min(ans, len(hard))
print(ans)