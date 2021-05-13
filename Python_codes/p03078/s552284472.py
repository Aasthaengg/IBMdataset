import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


x,y,z,K = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
ab = [(a[i]+b[j]) for i in range(x) for j in range(y)]
ab.sort(reverse=True)
c.sort(reverse=True)
abk = ab[:K]
ck = c[:K]
l = [(abk[i]+ck[j]) for i in range(min(len(abk),K)) for j in range(min(len(ck),K))]
l.sort(reverse=True)
write("\n".join(map(str, l[:K])))