import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = list(input())
odd = set(['R', 'U', 'D'])
even = set(['L', 'U', 'D'])

leng = len(S)
for i in range(leng):
    if i%2==1:
        if not S[i] in even:
            print('No')
            break
    else:
        if not S[i] in odd:
            print('No')
            break
else:
    print('Yes')