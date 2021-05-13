import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


m,k = map(int, input().split())
if k>=2**m:
    ans = -1
elif m==0:
    ans = "0 0"
elif m==1:
    if k==1:
        ans = -1
    else:
        ans = "0 1 1 0"
else:
    ans = list(range(2**m)) 
    ans1 = ans[:k] + ans[k+1:] + [k]
    ans2 = [k] + ans[:k] + ans[k+1:]
    ans = ans1 + ans2[::-1]
    ans = " ".join(map(str, ans))
print(ans)