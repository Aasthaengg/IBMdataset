n = int(input())
s = list(list(input().split()) for _ in range(n))
ans = [s.index(i)+1 for i in sorted(s, key=lambda x:(x[0], -int(x[1])))]
for i in ans: print(i)
