H,W = map(int,input().split())
ansls = []
ansls.append('#'*(W+2))
for i in range(H):
    ansls.append('#'+input()+'#')
ansls.append('#'*(W+2))
for i in range(H+2):
    print(ansls[i])