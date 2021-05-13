N = int(input())
A = set(map(int,input().split()))
def helper(A):
    v = min(A)
    ans = set()
    for a in A:
        if a%v!=0:
            ans.add(a%v)
    ans.add(v)
    return ans

while len(A)>1:
    A = helper(A)
print(min(A))