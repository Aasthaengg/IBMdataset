n =  int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
fill = 0
cnt = 0
for f in range(n):
    fill = fill + b[a[f] - 1]
    if(f != 0 and a[f] == a[f-1] + 1):
        fill = fill + c[a[f-1]-1]
        cnt = cnt + 1
    else:
        cnt = cnt + 1
print(fill)