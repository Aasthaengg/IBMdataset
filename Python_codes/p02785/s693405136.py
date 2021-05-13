N,K,*H = map(int, open(0).read().split())
H.sort(reverse=True)
print(sum(H[K:]))