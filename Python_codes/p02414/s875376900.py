import sys

def input_number():
    for i in range(n):
        adding=map(int,raw_input().split())
        A.append(adding)
    for i in range(m):
        adding=map(int,raw_input().split())
        B.append(adding)

if __name__ == '__main__':
    n,m,l=map(int,raw_input().split())
    A=[]
    B=[]
    ans=[[0 for j in range(l)]for i in range(n)]
    input_number()
    for i in range(n):
        for j in range(l):
            for k in range(m):
                ans[i][j] += A[i][k] * B[k][j]
    for i in range(n):
        for j in range(l):
            sys.stdout.write("%d" % ans[i][j])
            if j != l-1:
                sys.stdout.write(" ")
        sys.stdout.write("\n")