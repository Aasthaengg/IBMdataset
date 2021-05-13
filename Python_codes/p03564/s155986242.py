N=int(input())
K=int(input())
answer=1
for a in range(N):
    if answer*2>=answer+K:
        answer+=K
    else:
        answer*=2
print(answer)
