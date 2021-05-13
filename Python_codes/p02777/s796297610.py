S = list(map(str, input().split()))
I = list(map(int, input().split()))
U = input()
print(I[0] - (U == S[0]), I[1] - (U == S[1]))