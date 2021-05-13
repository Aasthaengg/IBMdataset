N = int(input())
T, A = map(int,input().split())
H = list(map(int, input().split()))

temp = 0
anslist = []
for i in range(N):
    temp = (T - H[i] * 0.006) - A
    anslist.append(abs(temp))

print(anslist.index(min(anslist))+1)