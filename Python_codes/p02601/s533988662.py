a, b,c = map(int, input().split())
K=int(input())

for i in range(K):
    if b<=a:
        b=b*2

    elif c<=b:
        c=c*2

    if a<b and b<c:
        print('Yes')
        exit()
print('No')
