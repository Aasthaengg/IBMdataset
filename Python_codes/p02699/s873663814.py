s,w=map(int, input().split())
k=0
if w>=s:
    k='unsafe'
if w<s:
    k='safe'
print(k)