n = int(raw_input())
S = map(int, raw_input().strip().split(' '))
q = int(raw_input())
T = map(int, raw_input().strip().split(' '))

def search(S,k):
    for s in S:
        if s == k:
            return True
    return False

c = 0
for t in T:
    if search(S,t): c += 1

print c