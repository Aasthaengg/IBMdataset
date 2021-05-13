stdin = open(0).read().split('\n')
N, K = map(int,stdin[0].split())
S = stdin[1]
l=list(S)
l[K-1]=l[K-1].lower()
print("".join(l))