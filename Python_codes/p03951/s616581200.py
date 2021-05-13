N = int(input())
S = input()
T = input()

for i in range(N):
    for j, t in enumerate(T[:N-i]):
        if S[j+i] == t:
            continue
        else:
            break
    else:
        print(N+i)
        break
else:
    print(2*N)
