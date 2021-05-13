n=list(map(int,input().split()))
s=set()
for x in n:
    s.add(x)
print("YES" if s=={1,9,7,4} else "NO")