K = int(input())
S = input()
S_list = list(S)

if K < len(S_list):
    print(S[:K] + "...")
else:
    print(S)