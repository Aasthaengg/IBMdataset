import sys
input = sys.stdin.readline
A,B=map(int,input().split())
a=[["#"]*100 for i in range(50)]
b=[["."]*100 for i in range(50)]


for i in range(A-1):
    a[2*(i//50)][2*(i%50)]="."
for i in range(B-1):
    b[2*(i//50)+1][2*(i%50)]="#"
print(100,100)
for i in a:
    print("".join(i))
for i in b:
    print("".join(i))
