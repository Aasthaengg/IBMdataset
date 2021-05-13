s = input()
K = int(input())

ln = len(s)
ans = set()

for i in range(K) :
    for j in range(ln-i) :
        ans.add(s[j:j+i+1])

ans2 = sorted(list(ans))
print(ans2[K-1])
