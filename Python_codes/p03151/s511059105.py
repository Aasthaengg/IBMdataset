N = int(input())
A = [int(hoge) for hoge in input().split()]
B = [int(hoge) for hoge in input().split()]
#Aiの総和を変えずに、なるべく少ない量のAiを変えて全部合格を目指す
if sum(B) > sum(A):
    print(-1)
else:
    diff = 0
    points = []
    ans = 0
    for i in range(N):
        a = A[i]
        b = B[i]
        if a < b:
            diff += b - a
            ans += 1
        elif a > b:
            points.append(a-b)
    for p in sorted(points,reverse = True):
        if diff <= 0:
            print(ans)
            exit()
        diff -= p
        ans += 1 
    print(ans)              