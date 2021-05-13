s = input()
k = int(input())
n = len(s)

ansset= set()
for i in range(1,k+1):
    for j in range(n-i+1):
        ansset.add(s[j:j+i])

anslist = sorted(list(ansset))

print(anslist[k-1])

