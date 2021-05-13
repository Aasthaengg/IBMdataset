

# https://atcoder.jp/contests/m-solutions2019/submissions/5738704


from collections import deque, _heapq

n = int(input())

g = [{"num":0,"neighber":[]} for _ in range(n+1) ]

for _ in range(n-1):

    a, b = map(int, input().split())

    g[a]["neighber"].append(b)
    g[b]["neighber"].append(a)


c = sorted( map(int, input().split()) )

# sum(c[:-1]) 
print( sum(c) - c[-1] )


i = 0
s = [(0,1)]

while i < len(s):
    
    pre, cur = s[i]
    i += 1

    g[cur]["num"] = c.pop()

    for e in g[cur]["neighber"]:
        if e == pre:
            continue

        s.append( (cur,e) )

ans = ''
for i in range(1,n+1):
    ans += str( g[i]["num"] ) + " "



print( ans[:-1] )


