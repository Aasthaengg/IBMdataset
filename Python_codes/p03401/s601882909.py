n = int(input())
a_ls = list(map(int, input().split()))
a_ls = [0] + a_ls
a_ls.append(0)

S = 0
for i in range(n+1):
    S += abs(a_ls[i] - a_ls[i+1])
for i in range(1,n+1):
    ans = S + abs(a_ls[i+1] - a_ls[i-1]) - (abs(a_ls[i-1] - a_ls[i]) + abs(a_ls[i] - a_ls[i+1]))
    print(ans)