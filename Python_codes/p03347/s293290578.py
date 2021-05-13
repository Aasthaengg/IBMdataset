N = int(input())

ans = 0
arr = [-1]
for i in range(N):
    A = int(input())
    if A > arr[i] + 1:
        print(-1)
        break
    if A == arr[i] + 1 and i != 0:
        ans += 1
    else:
        ans += A
    arr.append(A)
else:
    print(ans)
    
