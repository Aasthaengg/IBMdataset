n,k = map(int,input().split())
s = input()
compressed = []
prev = ""
for i in s:
    if i != prev:
        compressed.append(i)
        prev=i
happy=len(compressed)-1
print(n-1-max(0,happy-2*k))