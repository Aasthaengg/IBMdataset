n = int(input())
if n%2 == 1:
    a = n-1
else:
    a = n
ans = []
for i in range(a-1):
    for j in range(i+1,a):
        if i+j+2 == a+1:
            continue
        else:
            ans += [[i+1,j+1]]
            # print(i+1,j+1)
if n%2 == 1:
    for i in range(n-1):
        ans += [[i+1,n]]
        # print(i+1,n)
print(len(ans))
for i in ans:
    print(*i)