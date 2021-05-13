N = int(input())
A = [input() for i in range(N)]

prev = []
next = 0
count = 0
while(count < N):
    next = int(A[next])-1
    count += 1
    if(next == 1):
        print(count)
        break
else:
    print(-1)
