S = input()
mabs = 2000
for i in range(len(S)-2):
    if abs(int(S[i:i+3])-753) < mabs:
        mabs = abs(int(S[i:i+3])-753)
print(mabs)