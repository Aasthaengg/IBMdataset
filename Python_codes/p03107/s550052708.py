S=input()
zeros=S.count("0")
ones=S.count("1")
print(len(S)-abs(zeros-ones))
