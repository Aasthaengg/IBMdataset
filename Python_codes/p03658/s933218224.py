N, K = input().split()
N = int(N)
K = int(K)

l = input().split()

l_i = []
for s in l:
    l_i.append(int(s))
    
l_i.sort(reverse = True)

l_s = l_i[:K]

print(sum(l_s))