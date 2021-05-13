N = int(input())
A = list(map(int,(input().split())))
S = A #調べたいリスト

result={}
for i in range (0,len(S)):
    item = S[i]
    if item in result:
        result[item] = result[item]+1
    else:
        result[item] = 1

a = [k for k, v in result.items()]

h = []
for i in a:
    h.append(result[i]-1)

h.sort(reverse=True)

n = len(h)
for i in range(n):
    if h[i] >= 1:
        if h[i]%2 == 1:
            h[i] = 1
        else:
            h[i] = 0

if sum(h) % 2 == 0:
    print(n)
else:
    print(n-1)