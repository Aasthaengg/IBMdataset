A,B,C = map(int,input().split())
K = int(input())

ans = sum([A,B,C]) - max(A,B,C) + max(A,B,C)*pow(2,K)

print(ans)