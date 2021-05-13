N, A, B = map(int, input().split())

if abs(A-B) % 2 == 0:
    print(abs(A-B)//2)

else:
    ans1 = min(A, B) + (max(A, B)-min(A, B)-1)//2
    ans2 = N-max(A, B)+1 + (N-min(A, B) - (N-max(A, B)) -1)//2
    print(min(ans1, ans2))