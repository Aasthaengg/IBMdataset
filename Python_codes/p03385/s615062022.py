S = input()
if len(list(set((sorted(S))))) == 3:
    print('Yes')
else:
    print('No')
