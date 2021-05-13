S = input()
K = int(input())

lst = set()
for i in range(len(S)):
    for j in range(1, K+1):
        lst.add(S[i:i+j])

res = sorted(list(lst))
print(res[K-1])