import sys

def input_number():
    for i in range(n):
        adding=map(int,raw_input().split())
        A.append(adding)
    for i in range(m):
        adding=input()
        b.append(adding)

if __name__ == '__main__':
    n,m=map(int,raw_input().split())
    A=[]
    b=[]
    ans=[0 for i in range(n)]
    input_number()
    for i in range(n):
        for j in range(m):
            ans[i] += A[i][j] * b[j]
    for i in range(n):
        print ans[i]