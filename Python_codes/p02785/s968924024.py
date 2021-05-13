n, k = map(int,input().split())
h = list(map(int,input().split()))

h.sort(reverse = True)
t = 0

del h[0:k]
    
if len(h) == 0 :
    print(0)
else:
    t += sum(h)
    print(t)    