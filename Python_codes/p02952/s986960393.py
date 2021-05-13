N = int(input())
if 1 <= N <= 9:
    ans = N
elif 10 <= N <= 99:
    ans = 9
elif 100 <= N <= 999:
    ans = 9 + N - 99
elif 1000 <= N <= 9999:
    ans = 9 + 900
elif 10000 <= N <= 99999:
    ans = 9 + 900 + N - 9999
elif N == 100000:
    ans = 9 + 900 + 90000
print(ans)
