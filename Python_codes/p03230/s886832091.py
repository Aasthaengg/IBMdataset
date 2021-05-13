import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
for k in range(1,n+3):
    if k*(k-1)//2==n:
        print("Yes")
        print(k)
        size = (k-1)//2
#         l = [set() for _ in range(n)]
        l = [set() for _ in range(k)]
        ind  = 1
        for i in range(k):
            for j in range(i+1,k):
                l[i].add(ind)
                l[j].add(ind)
                ind += 1
                    
        for i in range(k):
            print(len(l[i]), " ".join(map(str, l[i])))
        break
else:
    print("No")