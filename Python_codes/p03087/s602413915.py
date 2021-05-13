n,q = map(int,input().split())
s = input()
inf = [0]*n
num = 0
for i in range(1,n):
    if s[i] == "C" and s[i-1] == "A":
        num += 1
    inf[i] += num
for i in range(q):
    a,b = map(int,input().split())
    print(inf[b-1] - inf[a-1])