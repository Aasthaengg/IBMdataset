n = int(input())
plot = [0]*n
ans = 0.0
for i in range(n):
    plot[i] = list(map(int,input().split()))
for i in range(n):
    for j in range(n-i-1):
        l = (plot[i][0]-plot[i+j+1][0])**2 + (plot[i][1]-plot[i+j+1][1])**2
        l = l ** 0.5
        ans += l*2
ans = ans/n
print(ans)