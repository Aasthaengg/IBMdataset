N = int(input())
li = [ int(it) for it in input().split() ]
li = [ li[i]-i-1 for i in range(N) ]
li.sort()

p = li[N//2]
pi = [ abs(it-p) for it in li ]
print ( sum(pi) )