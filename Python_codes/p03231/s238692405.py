n,m = map(int, input().split())
s = input()
t = input()

def lcd(n, m):
    # 最大公約数
    a = max(n,m)
    b = min(n,m)
    while b:
        a, b = b, a % b
    return n*m//a

l = lcd(n,m)
m1 = l//m
n1 = l//n

for i in range(n*m//l):
    a = m1*i 
    b = n1*i 
    if s[a] != t[b]:
        print(-1)
        exit()
print(l)