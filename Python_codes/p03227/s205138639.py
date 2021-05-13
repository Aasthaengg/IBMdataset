S = input()

if len(S) == 2:
    print(S)
else:
    print(S[-1:-len(S)-1:-1])