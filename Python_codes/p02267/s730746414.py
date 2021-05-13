n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = map(int, input().split())

def ls(A, k):
    for a in A:
        if k == a:
            return True
    return False

print(sum([ls(S, t) for t in T]))