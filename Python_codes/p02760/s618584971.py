a0 = list(map(int, input().split()))
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

n = int(input())
b = []
for _ in range(n):
    b.append(int(input()))

if a0[0] in b and a0[1] in b and a0[2] in b or a1[0] in b and a1[1] in b and a1[2] in b or a2[0] in b and a2[1] in b and a2[2] in b or  a0[0] in b and a1[0] in b and a2[0] in b or a0[1] in b and a1[1] in b and a2[1] in b or a0[2] in b and a1[2] in b and a2[2] in b or a0[0] in b and a1[1] in b and a2[2] in b or a0[2] in b and a1[1] in b and a2[0] in b:
    print('Yes')
else:
    print('No')
