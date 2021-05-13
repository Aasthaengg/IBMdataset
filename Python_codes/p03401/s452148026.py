N = int(input())
A = list(input().split())
locate = [int(A[i]) for i in range(N)]
locate.append(0)
locate.insert(0, 0)
ALL = sum([abs(locate[i+1]-locate[i]) for i in range(N+1)])

for i in range(1, N+1):
    left = locate[i] - locate[i-1]
    right = locate[i+1] - locate[i]
    if left*right < 0:
        print(ALL - 2 * min(abs(left), abs(right)))
    else:
        print(ALL)