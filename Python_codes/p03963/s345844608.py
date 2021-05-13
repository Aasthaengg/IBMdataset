N,K = [int(i) for i in input().split()]

ans = int(K*(K-1)**(N-1))

print(ans)