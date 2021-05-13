S = input()
print(len([i for i in range(len(S)) if 'CODEFESTIVAL2016'[i]!=S[i]]))