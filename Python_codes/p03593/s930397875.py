from collections import Counter
def check():
    H, W = map(int, input().split())
    S = ''
    for i in range(H):
        S += input()
    C = Counter(S)
    vmod4 = list(map(lambda x:x%4,C.values()))
    V = Counter(vmod4)
    two = (H%2)*(W//2)+(H//2)*(W%2)
    odd = (H%2)*(W%2)
    if V[2]<= two and V[1]+V[3]<=odd:
        return True
    return False
if check():
    print('Yes')
else:
    print('No')