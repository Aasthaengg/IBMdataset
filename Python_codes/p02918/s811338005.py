n, k = map(int, input().split())
s = input()

if n == 1:
    print(0)
    exit()

happy = 0
lchunk, rchunk = [], []
before = s[0]
if before == 'R' and s[1] == 'R':
    happy += 1
for i in range(1, n):
    si = s[i]

    if si != before:
        if before == 'L':
            if lchunk == [] and rchunk == []:
                lchunk.append(1)
            else:
                lchunk.append(2)
        else:
            if rchunk == [] and lchunk == []:
                rchunk.append(1)
            else:
                rchunk.append(2)
    
    if si == 'L' and s[i-1] == 'L':
        happy += 1
    if i < n-1:
        if si == 'R' and s[i+1] == 'R':
            happy += 1
    before = si
if s[-1] == 'L':
    lchunk.append(1)
else:
    rchunk.append(1)

lchunk.sort(reverse=True)
rchunk.sort(reverse=True)

if lchunk == [] or rchunk == []:
    print(happy)
else:
    print(max(happy+sum(lchunk[:k]), happy+sum(rchunk[:k])))