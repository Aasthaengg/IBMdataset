x,n = map(int, input().split())
p = set(map(int, input().split()))
for i in range(101):
    if x-i not in p:
        print(x-i)
        break
    if x+i not in p:
        print(x+i)
        break