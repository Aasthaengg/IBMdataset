import copy

def solve():
    V = copy.copy(v)
    while len(V) > 1:
#        print(V)
        V.sort()
        tmp = (V[0]+V[1])/2
        del V[0:2]
        V.append(tmp)
    print(V[0])


if __name__ == "__main__":
    N = int(input())
    v = list(map(float, input().split()))  
    solve()

