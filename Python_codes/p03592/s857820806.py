import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,m,k = list(map(int, input().split()))
ans = "No"
for i in range(n+1):
    for j in range(m+1):
        val = i*j + (n-i)*(m-j)# - i*(m-j) - j*(n-i)
#         print(val)
        if val==k:
            ans = "Yes"
            break
    if ans=="Yes":
        break
print(ans)