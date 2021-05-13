N,K,Q = map(int,input().split())

correct = [0]*N

for i in range(Q):
    winner = int(input()) - 1
    correct[winner] += 1


for i in range(N):
    score = K - (Q-correct[i])
    if score <= 0:
        print("No")
    else:
        print("Yes")