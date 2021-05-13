N = int(input())
A = list(map(int, input().split()))

student_arr = [(A[i], i) for i in range(N)]
student_arr.sort()

res = ''
for i in range(N):
    res += str(student_arr[i][1] + 1)
    if i < N - 1:
        res += ' '

print(res)