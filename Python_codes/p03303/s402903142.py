S = input()
N = int(input())
print(*(S[i] for i in range(0, len(S), N)), sep='')