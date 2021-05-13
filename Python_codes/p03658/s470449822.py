#ABC 067 B - Snake Toy
N,K = map(int,input().split())
ln = list(map(int,input().split()))

an = []
for i in range(K):
    an.append(max(ln))
    del ln[ln.index(max(ln))]

k = 0 
for i in range(len(an)):
    k += an[i]

print(str(k))