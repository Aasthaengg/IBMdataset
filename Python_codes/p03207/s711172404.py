n = int(input())
p = list(int(input()) for i in range(n))
p.sort(reverse = True)
s = p.pop(0) // 2
print(sum(p,s))