N = int(input())
S = input()
T = input()
kaburi = 0
for i in range(N):
    #sの末尾とtの先頭を比べる
    #print("sの末尾"+str(i+1)+"文字目"+S[-(i+1):])
    #print("Tの先頭"+str(i+1)+"文字目"+T[0:i+1])
    if S[-(i+1):] == T[0:i+1]:
        kaburi = len(S[-(i+1):])
print(2*N-kaburi)
