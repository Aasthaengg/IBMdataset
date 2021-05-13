n = int(input())
data = list(map(int,input().split()))
data.reverse()
for x in range(n):
    print(data[x],end='')
    if x!=n-1: print(' ',end='')
print()

