#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]


n,l = map(int, input().split())

taste = []
for i in range (1,n+1):
    taste.append(l+i-1)

if l < 0:
    if (-1)*l < n:
        print(sum(taste))
    else:
        del taste[-1]
        print(sum(taste))
else:
    #最初だけぬかす
    del taste[0]
    print(sum(taste))

