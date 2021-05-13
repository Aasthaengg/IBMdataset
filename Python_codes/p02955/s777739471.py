import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,k = list(map(int, input().split()))
a = list(map(int, input().split()))
s = sum(a)
def fs(n):
    s = set()
    for i in range(1,int(n**0.5)+2):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    l = sorted(list(s))
    return l
l = fs(s)
def sub(v):
    val0 = [item%v for item in a if item%v!=0]
    val1 = [(v-item)%v for item in val0]
    val0.sort()
    val1.sort(reverse=True)
#     print(val0,val1)
    i = 0
    j = len(val0)-1
    ans = 0
    while i<j:
        if val0[i]<val1[j]:
            val1[j] -= val0[i]
            ans += val0[i]
            i += 1
        else:
            val0[i] -= val1[j]
            ans += val1[j]
            j -= 1
    return ans
for v in reversed(l):
    if k>=sub(v):
        break
print(v)