n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))
def liner_search(S, key):
    for i in S:
        if i == key:
            return True
    return False
print(sum(liner_search(S, key) for key in T))
