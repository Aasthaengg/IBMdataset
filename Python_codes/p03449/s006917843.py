# coding: utf-8

N = int(input())
A = []
for _ in range(2):
    A.append(list(map(int, input().split(" "))))


def oritara(A, orirutoko):
    tmp = sum(A[0][:orirutoko+1])
    tmp += sum(A[1][orirutoko:])
    return tmp

ame = 0
for i in range(N):
    ame = max(oritara(A, i), ame)

print(ame)
