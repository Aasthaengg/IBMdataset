n=int(input())
w = [(input()) for _ in range(n)]
l = set(w)
if len(w) != len(l):
        print('No')
        exit()
for i in range(n-1):
        if w[i][len(w[i])-1] != w[i+1][0]:
                print('No')
                exit()
print('Yes')