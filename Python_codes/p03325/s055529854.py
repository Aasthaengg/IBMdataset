N = int(input())
a = list(map(int,input().split()))
ans = 0
for i in a :
    if i%2 == 0:
        for j in range(i):
            if i%2 == 1:
                break
            i = i/2
            ans += 1
print(int(ans))