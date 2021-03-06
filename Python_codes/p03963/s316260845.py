"""解説から
1. Bi(1<=i<=N)のボールの中の左端B1のボールに塗る色を決める(K通り)
2. 2<=i<=Nのボールの塗る色を順に決めていく
    この時、B(i-1)のボールと異なる色であれば何色で塗ってもよい(K-1通り)
3. 1と2の前提からK*(K-1)**(N-1)通りの塗り方ができる
"""
N, K = map(int, input().split())
print(K * (K - 1)**(N - 1))
