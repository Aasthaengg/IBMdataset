coin = [500,100,50]
a = int(input())
b = int(input())
c = int(input())
x = int(input())
ans = 0
for i_500 in range(a+1):
    for i_100 in range(b+1):
        for i_50 in range(c+1):
            if x==i_500*500+i_100*100+i_50*50:
                ans += 1
print(ans)
