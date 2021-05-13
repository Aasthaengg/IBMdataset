def readInt():
    return list(map(int,input().split()))
n,k = readInt()
l = readInt()
l.sort(reverse=True)
ans = sum(l[:k])
print(ans)