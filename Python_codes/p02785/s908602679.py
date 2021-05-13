n, k = map(int, input().split())
H = list(map(int, input().split()))

if k >= len(H):
    print(0)
    exit()

H.sort(reverse=True)

print(sum(H[k:]))
