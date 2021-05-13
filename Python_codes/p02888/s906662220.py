n = int(input())
l = list(map(int,input().split()))
l.sort(reverse=True)
ans = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        a = l[i]
        b = l[j]
        x = (a+1) - b
        y = (b+1) - a
        z = max(x,y)
        a = j+1
        b = n-1
        c = (a+b) // 2
        while a <= b:
            if l[c] == z:
                a += 1
            elif l[c] > z:
                a = c + 1
            elif l[c] < z:
                b = c - 1
            else:
                pass
            c = (a+b) // 2
        ans += c-j
print(ans)