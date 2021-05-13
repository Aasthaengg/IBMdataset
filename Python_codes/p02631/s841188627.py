N = int(input())
aaa = list(map(int, input().split()))
a_all = 0
for a in aaa:
    a_all ^= a
print(*list(a_all ^ a for a in aaa))
