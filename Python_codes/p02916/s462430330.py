n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
ans = sum(b)
for i in range(len(c)):
    try:
        if a[a.index(i+1)+1] == i+2:
            ans += c[i]
    except IndexError:
        pass
print(ans)