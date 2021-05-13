N = int(input())
A = [int(input()) for _ in range(N)]
ans, temp = 0, 0
for i in range(N-1, -1, -1):
    if A[i] < temp:
        print(-1)
        exit() 
    elif A[i] != 0:
        if A[i] == temp:
            temp -= 1    
        else:
            if i  >= A[i]:
                ans += A[i]
                temp = A[i] - 1
            else:
                print(-1)
                exit()
print(ans)