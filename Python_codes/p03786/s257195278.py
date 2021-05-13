N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)

sam = sum(A)
ans = 1
for i in range(0, N):
    sam -= A[i]
    if sam*2 >= A[i]:
        ans += 1
    else:
        break

print(ans)




