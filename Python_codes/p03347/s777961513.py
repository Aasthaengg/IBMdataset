n = int(input())
a = [int(input()) for i in range(n)]
a += [a[-1]]
def end():
    print(-1)
    exit()

if a[0] != 0:
    end()

ans = 0
for i in range(1, n+1):
    if a[i-1]+1 < a[i]:
        end()
    elif a[i-1] + 1 == a[i]:
        continue
    else:
        ans += a[i-1]
print(ans)