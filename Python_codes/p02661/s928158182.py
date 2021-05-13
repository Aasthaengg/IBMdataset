import numpy as np

def solve():
    N = int(input())
    AB = np.array([list(map(int, input().split() )) for _ in range(N)], dtype=np.int64)
    A = AB[:,0]
    B = AB[:,1]
    Amed = np.median(A)
    Bmed = np.median(B)
    if N % 2 ==1:
        print(int(Bmed - Amed+1))
    else:
        print(int((Bmed - Amed )*2+1))


if __name__ == '__main__':
    solve()