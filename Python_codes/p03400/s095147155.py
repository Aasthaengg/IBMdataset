N = int(input())
D,X = map(int, input().split())
an  = N
for i in range(N):
    x = int(input())
    an += (D-1)//x
print(an+X)