import sys
input = sys.stdin.readline

S=input().strip()

N = len(S)//2
i = 0
while True:
    i += 1
    a = S[0:(N-i)]
    b = S[(N-i):(2*N-2*i)]
    if a == b:
        print(len(a)*2)
        exit()
