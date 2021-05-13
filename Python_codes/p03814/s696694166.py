S = input()
start = S.find('A')
end = S.rfind('Z')
print(len(S[start:end])+1)