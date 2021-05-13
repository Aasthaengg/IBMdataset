A,B,C = map(int,input().split())
K = int(input())
L = [A,B,C]
maxL = max(L)
L.remove(maxL)
print(maxL*2**K + sum(L))