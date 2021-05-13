import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


k = int(input())
a = list(map(int, input().split()))
v1 = 2
v2 = 2
ans = None
for num in a[::-1]:
#     print(v1,v2)
    # num人組を作って生き残れた人がv1~v2人
    if (v1-1)//num == (v2)//num:
        ans = -1
        break
    v1 = ((v1-1)//num+1) * num
    v2 = (v2)//num * num + (num-1)
if ans == -1:
    print(ans)
else:
    print(v1,v2)