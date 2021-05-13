from itertools import product
def solve():
    N,A,B,C = map(int,input().split())
    models = [A,B,C]
    l = [int(input()) for _ in range(N)]

    comb = list(product([-1,0,1,2],repeat=N))

    mn = float('inf')
    for c in comb:
        sm = 0
        for i in range(3):
            elements = []
            for j in range(N):
                if c[j] == i:
                    elements.append(l[j])
            
            if len(elements) == 0:
                break
            sm += (len(elements) - 1) * 10
            sm += abs(models[i] - sum(elements))
        else:
            mn = min(mn, sm)
    
    print(mn)

if __name__ == '__main__':
    solve()