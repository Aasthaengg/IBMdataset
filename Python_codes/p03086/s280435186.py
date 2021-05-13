#n = int(input())
#n, k = map(int, input().split())
#al = list(map(int, input().split()))
#al=[list(input()) for i in range(h)]
s = list(input())


def isACGT(s):
    A = s.count('A')
    C = s.count('C')
    G = s.count('G')
    T = s.count('T')
    if A+C+G+T == len(s):
        return True
    else:
        return False


ans = 0
n = len(s)
for i in range(n):
    for j in range(i, n):
        tempstring = s[i:j+1]
        if isACGT(tempstring):
            ans = max(ans, len(tempstring))
print(ans)
