import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
l = list(map(int, input().split()))
l.sort(reverse=True)
def sub(x):
    j = n-1
    ans = 0
    for i in range(x+1, n-1):
        if j<=i:
            break
        while j-1>i and l[i]+l[j]<=l[x]:
            j -= 1
        if i<j and l[i]+l[j]>l[x]:
            ans += (j-i)
#         print(i,j)
    return ans
ans = 0
for x in range(n-2):
    ans += sub(x)
#     print(ans)
print(ans)