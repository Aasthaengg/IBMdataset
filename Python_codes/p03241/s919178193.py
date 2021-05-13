n,m = map(int,input().split())
div = []
for i in range(1,int(m**0.5)+1):
    if m%i == 0:
        div.append(i)
        div.append(m//i)
div.sort(reverse=True)
for x in div:
    if m//x >= n:
        print(x)
        break