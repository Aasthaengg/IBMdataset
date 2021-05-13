import sys
input = sys.stdin.readline

N,K=map(int,input().split())

print(K*(K-1)**(N-1))