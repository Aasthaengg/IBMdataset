h,w = map(int,input().split())
C = [["#" for j in range(w+2)] for i in range(h+2)]
for i in range(h):
    C[i+1][1:] = list(input()) + ["#"]
for i in range(h+2):
    print("".join(C[i][:]))